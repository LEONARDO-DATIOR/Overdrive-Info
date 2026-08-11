import customtkinter as customTK

from machine_monitor.collectors.DiskCollector import DiskCollector
from machine_monitor.gui.pages.components.texts.TituloPrincipal import TituloPrincipal

class DiskInfoView(customTK.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        print("Gerando relatório de SSD/HD...")

        self.info_disco = TituloPrincipal(
            master=self,
            text="Informações de Disco"
        )
        self.info_disco.pack(pady=10)

        discos = DiskCollector().collect()

        self.frame_disco = customTK.CTkScrollableFrame(
            self,
            width=600,
            height=300,
        )

        self.frame_disco.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )
        for disco in discos:

            # CARD / DIV
            info_card = customTK.CTkFrame(
                self.frame_disco,
                width=500,
                height=200,
                corner_radius=15,
                fg_color="#1E1E1E"
            )

            info_card.pack(
                pady=20,
                padx=20,
                fill="x"
            )

            # TÍTULO
            titulo = customTK.CTkLabel(
                info_card,
                text=disco.unidade,
                font=("Arial", 20, "bold")
            )

            titulo.pack(
                pady=(20, 10)
            )

            # TEXTO 1
            cpu = customTK.CTkLabel(
                info_card,
                text=f"Capacidade: {disco.get_total_bytes()} GB",
                font=("Arial", 14)
            )

            cpu.pack(
                anchor="w",
                padx=20,
                pady=5
            )

            # TEXTO 2
            memoria = customTK.CTkLabel(
                info_card,
                text=f"Utilizando: {disco.get_usados_bytes()} GB",
                font=("Arial", 14)
            )

            memoria.pack(
                anchor="w",
                padx=20,
                pady=5
            )

            # TEXTO 3
            sistema = customTK.CTkLabel(
                info_card,
                text=f"Disponível: {disco.get_livre_bytes()} GB",
                font=("Arial", 14)
            )

            sistema.pack(
                anchor="w",
                padx=20,
                pady=5
            )

    def remover_frame(self):
        print("Removendo frame de informações de disco...")
        print(self.frame_disco)
        if self.frame_disco is not None and self.info_disco is not None:
            self.frame_disco.destroy()
            self.info_disco.destroy()
    