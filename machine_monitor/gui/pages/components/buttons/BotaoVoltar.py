import customtkinter as ctk

class BotaoVoltar(ctk.CTkButton): 

    def __init__(self, master, text, command):
        super().__init__(
            master,
            text=text,
            command=command,

            # Visual do botão
            width=50,
            height=30,

            fg_color="#253C50",
            hover_color="#09213D",
            text_color="white",

            corner_radius=18,
            border_width=2,
            border_color="#35424D"
        )

        
