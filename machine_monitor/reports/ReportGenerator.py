from datetime import datetime
from html import escape
from pathlib import Path

from playwright.sync_api import sync_playwright

from machine_monitor.collectors.SystemCollectors import SystemCollectors
from machine_monitor.collectors.ProcessorCollector import ProcessorCollector


class ReportGenerator:
    def __init__(
        self,
        output_dir: Path | str = "relatorios",
        system_collector: SystemCollectors | None = None,
        processor_collector: ProcessorCollector | None = None,
    ) -> None:
        self.output_dir = Path(output_dir)
        self.system_collector = system_collector or SystemCollectors()
        self.processor_collector = processor_collector or ProcessorCollector()

    def generate(self) -> Path:
        sistema = self.system_collector.get_system_info()
        processador = self.processor_collector.collect()
        caminho_salvo = self.carregar_caminho_relatorio()
        html = self._carregar_html(sistema, processador)

        self.output_dir.mkdir(parents=True, exist_ok=True)
        self._salvar_pdf(html, caminho_salvo)

        return caminho_salvo

    def _salvar_pdf(self, html: str, caminho_salvo: Path) -> None:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch()
            page = browser.new_page()
            page.set_content(html, wait_until="networkidle")
            page.pdf(
                path=str(caminho_salvo),
                format="A4",
                print_background=True,
                margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
            )
            browser.close()

    def carregar_caminho_relatorio(self) -> Path:
        sistema = self.system_collector.get_system_info()
        return self.output_dir / f"relatorio_sistema_{sistema.hostname}.pdf"

    def _carregar_html(self, sistema, processador) -> str:
        caminho = (
            Path(__file__).parent
            / "template"
            / "relatorio.html"
        )

        html = caminho.read_text(encoding="utf-8")

        html = (
            html
            .replace("{{SISTEMA}}", escape(sistema.sistema_operacional))
            .replace("{{VERSAO}}", escape(sistema.versao))
            .replace("{{HOSTNAME}}", escape(sistema.hostname))
            .replace("{{PROCESSADOR_NOME}}", escape(processador.processador))
        )

        return html