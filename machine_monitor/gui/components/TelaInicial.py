import customtkinter as customTK


class TelaInicial(customTK.CTkFrame):

    def __init__(self, master, formulario_relatorio, tela_opcoes):
        super().__init__(master)
        # TITULO
        titulo = customTK.CTkLabel(
            self,
            text="Overdrive-Info",
            font=("Arial", 24, "bold")
        )

        titulo.pack(pady=30)

        # BOTAO TELA DE OPÇÕES
        btn_opcoes = customTK.CTkButton(
            self,
            text="Informações especificas",
            command=tela_opcoes
        )
        btn_opcoes.pack(pady=10)

        # BOTAO TELA DO FORMULARIO RELATORIO
        btn_relatorio = customTK.CTkButton(
            self,
            text="Gerar Relatório",
            command=formulario_relatorio
        )

        btn_relatorio.pack(pady=10)