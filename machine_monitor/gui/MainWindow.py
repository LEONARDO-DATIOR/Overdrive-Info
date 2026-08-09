import customtkinter as ctk

from machine_monitor.gui.components.TelaOpcoes import TelaOpcoes
from machine_monitor.gui.components.TelaInicial import TelaInicial
from machine_monitor.gui.components.FormRelatorio import FormRelatorio


class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Windows System Report")
        self.geometry("900x600")

        self.tela_atual = None

        self.mostrar_tela_inicial()

    def limpar_tela(self):
        if self.tela_atual is not None:
            self.tela_atual.destroy()

    # ABRIR TELA INCIAL
    def mostrar_tela_inicial(self):
        self.limpar_tela()

        self.tela_atual = TelaInicial(
            self,
            formulario_relatorio=self.mostrar_tela_relatorio,
            tela_opcoes=self.mostrar_tela_opcoes
        )

        self.tela_atual.pack(
            fill="both",
            expand=True
        )

    # ABRIR TELA OPÇÕES
    def mostrar_tela_opcoes(self):
        self.limpar_tela()

        self.tela_atual = TelaOpcoes(
            self,
            voltar=self.mostrar_tela_inicial
        )

        self.tela_atual.pack(
            fill="both",
            expand=True
        )

    # ABRIR TELA RELATÓRIO
    def mostrar_tela_relatorio(self):
        self.limpar_tela()

        self.tela_atual = FormRelatorio(
            self,
            voltar=self.mostrar_tela_inicial
        )

        self.tela_atual.pack(
            fill="both",
            expand=True
        )