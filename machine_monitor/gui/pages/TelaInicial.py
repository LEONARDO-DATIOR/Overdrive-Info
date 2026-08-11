import customtkinter as customTK

from machine_monitor.gui.pages.components.texts.TituloPrincipal import TituloPrincipal


class TelaInicial(customTK.CTkFrame):

    def __init__(self, master, formulario_relatorio, tela_opcoes):
        super().__init__(master)
        # TITULO
        titulo = TituloPrincipal(
            master=self,
            text="Overdrive-Info"
        )

        titulo.pack(pady=30)

        # DESCRIÇÃO
        descricao = customTK.CTkLabel(
            self,
            text="Bem-vindo ao Overdrive-Info, o software que fornece informações detalhadas sobre o seu sistema operacional Windows. Com ele, você pode gerar relatórios completos sobre o desempenho do seu computador, incluindo informações sobre CPU, memória RAM, disco rígido e muito mais.",
            font=("Arial", 16),
            wraplength=600,
            justify="center"
        )
        descricao.pack(pady=20)

        # FRAME PRINCIPAL
        frame_tela_inicial = customTK.CTkFrame(
            self, 
            width=300, 
            height=300, 
            corner_radius=15,
        )
        frame_tela_inicial.pack()

        # BOTAO TELA DE OPÇÕES
        btn_opcoes = customTK.CTkButton(
            frame_tela_inicial,
            text="Informações especificas",

            # visual
            width=200,
            height=200,

            fg_color="#253C50",
            hover_color="#09213D",
            text_color="white",

            corner_radius=18,
            border_width=2,
            border_color="#35424D",


            # ação
            command=tela_opcoes
        )
        btn_opcoes.grid(row=0, column=0, padx=10)

        # BOTAO TELA DO FORMULARIO RELATORIO
        btn_relatorio = customTK.CTkButton(
            frame_tela_inicial,
            text="Gerar Relatório",

            # visual
            width=200,
            height=200,

            fg_color="#253C50",
            hover_color="#09213D",
            text_color="white",

            corner_radius=18,
            border_width=2,
            border_color="#35424D",

            # ação
            command=formulario_relatorio
        )
        btn_relatorio.grid(row=0, column=1, padx=10)
