from datetime import datetime
from html import escape
from pathlib import Path
import webbrowser

from jinja2 import Environment, FileSystemLoader
from playwright.sync_api import sync_playwright

from machine_monitor.collectors.DiskCollector import DiskCollector
from machine_monitor.collectors.SystemCollectors import SystemCollectors
from machine_monitor.collectors.ProcessorCollector import ProcessorCollector
from machine_monitor.collectors.MemoryCollector import MemoryCollector
from machine_monitor.collectors.SoftwaresCollectors import SoftwaresCollectors



class ReportGenerator:
    def __init__(
        self,
        output_dir: Path | str = "relatorios",
        system_collector: SystemCollectors | None = None,
        processor_collector: ProcessorCollector | None = None,
        disk_collector: DiskCollector | None = None,
        memory_collector: MemoryCollector | None = None,
        softwares_collector: SoftwaresCollectors | None = None,
    ) -> None:
        self.output_dir = Path(output_dir)
        self.system_collector = system_collector or SystemCollectors()
        self.processor_collector = processor_collector or ProcessorCollector()
        self.disk_collector = disk_collector or DiskCollector()
        self.memory_collector = memory_collector or MemoryCollector()
        self.softwares_collector = softwares_collector or SoftwaresCollectors()

    def gerar(self) -> Path:
        sistema = self.system_collector.get_system_info()
        processador = self.processor_collector.collect()
        memorias = self.memory_collector.collect()
        discos = self.disk_collector.collect()
        softwares = self.softwares_collector.collect()

        caminho_salvo = self.carregar_caminho_relatorio_html()
        html = self._carregar_html(sistema, processador, memorias, discos, softwares)

        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.salvar_html(html, caminho_salvo)
        webbrowser.open(caminho_salvo.resolve().as_uri())

        return caminho_salvo

    def salvar_html(self, html: str, caminho_salvo: Path) -> None:
        caminho_salvo.write_text(html, encoding="utf-8")

    def carregar_caminho_relatorio_html(self) -> Path:
        sistema = self.system_collector.get_system_info()
        return self.output_dir / f"relatorio_sistema_{sistema.hostname}.html"


    def _carregar_html(self, sistema, processador, memorias, discos, softwares) -> str:
        pasta_templates = Path(__file__).parent / "template"
        css = ( Path(__file__).parent / "styles" / "relatorioStyle.scss").read_text(encoding="utf-8")

        env = Environment(
            loader=FileSystemLoader(pasta_templates)
        )

        template = env.get_template("relatorio.html")


        html = template.render(
            sistema=sistema,
            processador=processador,
            memorias=memorias,
            discos=discos,
            css=css,
            softwares=softwares,
            data_geracao=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        )

        return html
    
    # PARA SALVAR COMO PDF
    # def _salvar_pdf(self, html: str, caminho_salvo: Path) -> None:
    #     with sync_playwright() as playwright:
    #         browser = playwright.chromium.launch()
    #         page = browser.new_page()
    #         page.set_content(html, wait_until="networkidle")
    #         page.pdf(
    #             path=str(caminho_salvo),
    #             format="A4",
    #             print_background=True,
    #             margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
    #         )
    #         browser.close()
    #  
    #   def carregar_caminho_relatorio_pdf(self) -> Path:
    #     sistema = self.system_collector.get_system_info()
    #     return self.output_dir / f"relatorio_sistema_{sistema.hostname}.pdf"