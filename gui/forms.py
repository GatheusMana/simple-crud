import tkinter as tk
from app import *
from styles import *

class TemplateWindow(tk.Toplevel):
    def __init__(self, base):
        super().__init__(base)
        self.geometry(window_geometry_size)
        
        # 1. Configuração comum a todas as janelas
        tk.Label(self, text="--- CRUD SYSTEM ---").pack(pady = (0,20))
        
        # 2. O PONTO DO POLIMORFISMO:
        # Chamamos um método que NÃO ESTÁ definido aqui com conteúdo,
        # mas que os filhos VÃO definir.
        self.generate_widgets()
        
        # 3. Outro elemento comum
        tk.Button(self, text="Exit",command=self.destroy).pack(side="bottom", pady=15)


class MainWindow(TemplateWindow):
    def __init__(self, base):
        super().__init__(base)
    
    def generate_widgets(self):
        self.insert_button = tk.Button(self, text="Insert Employee", width=template_window['BUTTON_WIDTH'], command= lambda: forms.InsertEmployeeWindow(self))
        self.insert_button.pack(pady=template_window['BUTTON_PADY'])

        self.read_one_employee_button = tk.Button(self, text="Read One Employee", width=template_window['BUTTON_WIDTH'], command= lambda: forms.ReadOneEmployeeWindowEmployeeWindow(self))
        self.read_one_employee_button.pack(pady=template_window['BUTTON_PADY'])

        self.read_all_employees_button = tk.Button(self, text="Read All Employee", width=template_window['BUTTON_WIDTH'], command= lambda: forms.ReadAllEmployeeWindowEmployeeWindow(self))
        self.read_all_employees_button.pack(pady=template_window['BUTTON_PADY'])

        self.update_employee_button = tk.Button(self, text="Update Employee", width=template_window['BUTTON_WIDTH'], command= lambda: forms.UpdateEmployeeWindowEmployeeWindow(self))
        self.update_employee_button.pack(pady=template_window['BUTTON_PADY'])

        self.delete_employee_button = tk.Button(self, text="Delete Employee", width=template_window['BUTTON_WIDTH'], command= lambda: forms.DeleteEmployeeWindowEmployeeWindow(self))
        self.delete_employee_button.pack(pady=template_window['BUTTON_PADY'])

class InsertEmployeeWindow(TemplateWindow):
    ...

class ReadOneEmployeeWindow(TemplateWindow):
    ...

class ReadAllEmployeeWindow(TemplateWindow):
    ...

class UpdateEmployeeWindow(TemplateWindow):
    ...

class DeleteEmployeeWindow(TemplateWindow):
    ...

if __name__ == '__main__':
    janela = App()
    janela.mainloop()
