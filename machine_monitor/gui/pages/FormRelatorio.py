import customtkinter as customTK

from machine_monitor.gui.pages.components.buttons.BotaoVoltar import BotaoVoltar
from machine_monitor.gui.pages.components.buttons.BotaoPrincipal import BotaoPrincipal
from machine_monitor.gui.pages.components.inputs.InputTexto import InputTexto
from machine_monitor.gui.pages.components.texts.TituloPrincipal import TituloPrincipal
from machine_monitor.reports.ReportGenerator import ReportGenerator


class FormRelatorio(customTK.CTkFrame):

    def __init__(self, master, voltar):
        super().__init__(master)
        self.voltar = voltar

        # TITULO
        titulo = TituloPrincipal(
            master=self,
            text="Gerar Relatório"
        )
        titulo.pack(pady=30)

        # BOTAO VOLTAR
        BotaoVoltar(
            master=self,
            text="Voltar",
            command=self.voltar,
        ).pack(anchor="w", padx=10, pady=10)
        
        # INPUT nome_cliente
        input_nome_cliente = InputTexto(
            master=self,
            label_text="Nome do colaborador: "
        )

        # INPUT analista_responsável
        input_analista_responsavel = InputTexto(
            master=self,
            label_text="Nome do analista responsável: "
        )

        # BOTAO GERAR RELATORIO
        btn_relatorio = BotaoPrincipal(
            master=self,
            text="Gerar Relatório",
            command=lambda: self.gerar_relatorio(
                input_nome_cliente.get_input(),
                input_analista_responsavel.get_input()
            )
        )
        btn_relatorio.pack(pady=10)


    def gerar_relatorio(self, nome_cliente, nome_analista):
        print("Gerando relatório...")
        print(f"Nome do colaborador: {nome_cliente}")
        print(f"Nome do analista: {nome_analista}")
        report_path = ReportGenerator().gerar(nome_cliente, nome_analista)
        print(f"Relatório gerado com sucesso no caminho: {report_path.resolve()}")