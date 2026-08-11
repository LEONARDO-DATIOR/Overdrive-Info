import customtkinter as ctk

class TituloPrincipal(ctk.CTkLabel):
    def __init__(self, master, text):
        super().__init__(
            master, 
            text=text, 
            font=("Arial", 28, "bold"),
            text_color="#4FC3F7"
        )