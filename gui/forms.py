import tkinter as tk
from app import *

class TemplateWindow(tk.Toplevel):
    def __init__(self, base):
        super().__init__(base)
        self.geometry(window_geometry_size)
        
        # 1. Configuração comum a todas as janelas
        tk.Label(self, text="--- CRUD SYSTEM ---").pack()
        
        # 2. O PONTO DO POLIMORFISMO:
        # Chamamos um método que NÃO ESTÁ definido aqui com conteúdo,
        # mas que os filhos VÃO definir.
        self.montar_corpo()
        
        # 3. Outro elemento comum
        tk.Button(self, text="Sair", command=self.destroy).pack(side="bottom")


if __name__ == '__main__':
    teste = TemplateWindow(App())
    teste.mainloop()
