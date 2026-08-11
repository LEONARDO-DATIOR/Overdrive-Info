import customtkinter as ctk

class BotaoPrincipal(ctk.CTkButton): 

    def __init__(self, master, text, command, width=200, height=50):
        super().__init__(
            master,
            text=text,
            command=command,

            # Visual do botão
            width=width,
            height=height,

            fg_color="#253C50",
            hover_color="#09213D",
            text_color="white",

            corner_radius=18,
            border_width=2,
            border_color="#35424D"
        )
