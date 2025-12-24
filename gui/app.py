import tkinter as tk
from styles import *


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Crud")
        
        self.geometry(window_geometry_size)
        self.resizable(False, False)

        self.generate_widgets()

    def generate_widgets(self):
        self.welcome_label = tk.Label(self, text="Welcome to Simple Crud!", font=(title_font_style))
        self.welcome_label.pack(pady=20, expand=True)

        self.enter_button = tk.Button(self, text="Enter", width=main_window['BUTTON_WIDTH'])
        self.enter_button.pack(pady=main_window['BUTTON_PADY'])    

        self.exit_button = tk.Button(self, text="Exit", width=main_window['BUTTON_WIDTH'], command=self.destroy)
        self.exit_button.pack(pady=main_window['BUTTON_PADY'])

        self.autor_label = tk.Label(self, text="made by: Gathana", font=(autor_font_style))
        self.autor_label.pack(pady=50)


if __name__ == '__main__':
    janela = App()
    janela.mainloop()