import customtkinter as customTK

from machine_monitor.gui.pages.components.DiskInfo import DiskInfoView

class TelaOpcoes(customTK.CTkFrame):

    def __init__(self, master, voltar):
        super().__init__(master)
        self.voltar = voltar
        self.disk_info_view = None
        def voltar_tela():
            if self.disk_info_view:
                self.disk_info_view.remover_frame()
            self.voltar()

        # TITULO DA TELA
        titulo = customTK.CTkLabel(
            self,
            text="Gerar Relatório",
            font=("Arial", 24, "bold")
        )
        titulo.pack(pady=20)

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
            command=voltar_tela
        )
        btn_voltar.pack(
            anchor="w",
            padx=10,
            pady=10
        )

        # ESCOLHA DO TIPO DE RELATÓRIO
        tipo_relatorio = customTK.CTkComboBox(
            self,
            values=[
                "Relatório de disco",
                "Relatório de Software",
                "Relatório Completo"
            ],
            width=300
        )

        tipo_relatorio.pack(pady=10)

        # BOTAO GERAR RELATÓRIO
        btn_gerar_relatorio = customTK.CTkButton(
            self,
            text="Gerar Relatório",
            command=lambda: self.gerar_informacoes(tipo_relatorio)
        )
        btn_gerar_relatorio.pack(pady=20)

        # TELA DE INFORMAÇÕES ESPECIFICAS
    def gerar_informacoes(self, tipo_relatorio):
        if self.disk_info_view:
            self.disk_info_view.remover_frame()

        match tipo_relatorio.get():
            case "Relatório de disco":
                self.disk_info_view = DiskInfoView(self)
                self.disk_info_view.pack(fill="both", expand=True)
            case "Relatório de Software":
                print("Gerando relatório de Software...")
            case "Relatório Completo":
                print("Gerando relatório Completo...")
            case _:
                print("Tipo de relatório inválido.")