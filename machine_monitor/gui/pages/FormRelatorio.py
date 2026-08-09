import customtkinter as customTK

from machine_monitor.reports.ReportGenerator import ReportGenerator


class FormRelatorio(customTK.CTkFrame):

    def __init__(self, master, voltar):
        super().__init__(master)
        self.voltar = voltar

        # TITULO
        titulo = customTK.CTkLabel(
            self,
            text="Windows System Report",
            font=("Arial", 24, "bold")
        )
        titulo.pack(pady=30)

        # BOTAO VOLTAR
        btn_voltar = customTK.CTkButton(
            self,
            text="Voltar",

            # Visual do botão
            width=50,
            height=25,

            fg_color="#253C50",
            hover_color="#09213D",
            text_color="white",

            corner_radius=18,
            border_width=2,
            border_color="#35424D",

            # Ação do botão
            command=voltar
        )
        btn_voltar.pack(
            anchor="w",
            padx=10,
            pady=10
        )

        # INPUT nome_cliente
        customTK.CTkLabel(
            self,
            text="Nome do colaborador: ",
        ).pack(pady=1)

        input_nome_cliente = customTK.CTkTextbox(
            self,
            width=400, 
            height=20,
            corner_radius=2
        )
        input_nome_cliente.pack(pady=10)

        # INPUT analista_responsável
        customTK.CTkLabel(
            self,
            text="Análista Responsável: "
        ).pack(pady=1)
        input_analista_responsavel = customTK.CTkTextbox(
            self,
            width=400,
            height=20,
            corner_radius=2
        )
        input_analista_responsavel.pack(pady=10)

        # BOTAO GERAR RELATORIO
        btn_relatorio = customTK.CTkButton(
            self,
            text="Gerar Relatório",
            command=lambda: self.gerar_relatorio(input_nome_cliente.get("0.0", "end"), input_analista_responsavel.get("0.0", "end"))
        )
        btn_relatorio.pack(pady=10)


    def gerar_relatorio(self, nome_cliente, nome_analista):
        print("Gerando relatório...")
        print(f"Nome do colaborador: {nome_cliente}")
        print(f"Nome do analista: {nome_analista}")
        report_path = ReportGenerator().gerar(nome_cliente, nome_analista)
        print(f"Relatório gerado com sucesso no caminho: {report_path.resolve()}")