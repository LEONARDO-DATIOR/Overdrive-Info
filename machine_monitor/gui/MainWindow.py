import customtkinter as customTK

from machine_monitor.gui.components.FormRelatorio import FormRelatorio



class MainWindow(customTK.CTk):

    def __init__(self):
        super().__init__()

        self.title("Windows System Report")
        self.geometry("700x400")

        form = FormRelatorio(self)
        form.pack(fill="both", expand=True)
    

    