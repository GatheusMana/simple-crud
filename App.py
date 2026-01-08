#App.py
import tkinter as tk
from gui.Forms import AppWindow
from DatabaseManager import DatabaseManager

if __name__ == '__main__':
    db_setup = DatabaseManager("data.db")
    
    janela = AppWindow()
    janela.mainloop()