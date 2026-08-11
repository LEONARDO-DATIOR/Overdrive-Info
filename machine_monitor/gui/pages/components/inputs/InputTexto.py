import customtkinter as ctk

class InputTexto(ctk.CTkEntry):
    def __init__(self, master, label_text):
        super().__init__(master)


        self.label = ctk.CTkLabel(
            master=master,
            text=label_text,
        )
        self.label.pack()

        self.input_text = ctk.CTkTextbox(
            master=master,
            width=400, 
            height=20,
            corner_radius=2
        )
        self.input_text.pack()

    def get_input(self):
        return self.input_text.get("1.0", "end-1c")