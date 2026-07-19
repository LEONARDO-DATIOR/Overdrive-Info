import customtkinter as customTK

from machine_monitor.reports.ReportGenerator import ReportGenerator


class FormRelatorio(customTK.CTkFrame):

    def __init__(self, master):
        super().__init__(master)


        titulo = customTK.CTkLabel(
            self,
            text="Windows System Report",
            font=("Arial", 24, "bold")
        )
        titulo.pack(pady=20)

        btn_relatorio = customTK.CTkButton(
            self,
            text="Gerar Relatório",
            command=self.gerar_relatorio
        )
        btn_relatorio.pack(pady=10)


    def gerar_relatorio(self):
        print("Gerando relatório...")
        report_path = ReportGenerator().gerar()
        print(f"Relatório gerado com sucesso no caminho: {report_path.resolve()}")