import customtkinter as customTK

from machine_monitor.gui.pages.components.DiskInfo import DiskInfoView
from machine_monitor.gui.pages.components.buttons.BotaoPrincipal import BotaoPrincipal
from machine_monitor.gui.pages.components.texts.TituloPrincipal import TituloPrincipal

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
        titulo = TituloPrincipal(
            master=self,
            text="Informações Específicas"
        )
        titulo.pack(pady=20)

        # BOTAO VOLTAR
        btn_voltar = BotaoPrincipal(
            master=self,
            text="Voltar",
            command=voltar_tela,
            width=50,
            height=30,
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
        btn_gerar_relatorio = BotaoPrincipal(
            master=self,
            text="Gerar Relatório",
            command=lambda: self.gerar_informacoes(tipo_relatorio),
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