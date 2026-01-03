import tkinter as tk
from app import *
from styles import *

class TemplateWindow(tk.Toplevel):
    def __init__(self, base):
        super().__init__(base)
        self.geometry(window_geometry_size)

        #Abstract func to generete widgets
        self.generate_widgets()

        #Back Button
        tk.Button(self, text="Exit",command=self.destroy).pack(side="bottom", pady=15)


class MainWindow(TemplateWindow):
    def __init__(self, base):
        super().__init__(base)

    def generate_widgets(self):
        self.title("Crud System")

        self.insert_button = tk.Button(self, text="Insert Employee", width=template_window['BUTTON_WIDTH'], command= lambda: InsertEmployeeWindow(self))
        self.insert_button.pack(pady=(30,5))

        self.read_one_employee_button = tk.Button(self, text="Read One Employee", width=template_window['BUTTON_WIDTH'], command= lambda: forms.ReadOneEmployeeWindowEmployeeWindow(self))
        self.read_one_employee_button.pack(pady=template_window['BUTTON_PADY'])

        self.read_all_employees_button = tk.Button(self, text="Read All Employee", width=template_window['BUTTON_WIDTH'], command= lambda: forms.ReadAllEmployeeWindowEmployeeWindow(self))
        self.read_all_employees_button.pack(pady=template_window['BUTTON_PADY'])

        self.update_employee_button = tk.Button(self, text="Update Employee", width=template_window['BUTTON_WIDTH'], command= lambda: forms.UpdateEmployeeWindowEmployeeWindow(self))
        self.update_employee_button.pack(pady=template_window['BUTTON_PADY'])

        self.delete_employee_button = tk.Button(self, text="Delete Employee", width=template_window['BUTTON_WIDTH'], command= lambda: forms.DeleteEmployeeWindowEmployeeWindow(self))
        self.delete_employee_button.pack(pady=template_window['BUTTON_PADY'])


class InsertEmployeeWindow(TemplateWindow):
    def __init__(self,base):
        super().__init__(base)

    def generate_widgets(self):
        self.title("Insert Employee")

        self.name_label = tk.Label(self, text="Employee Name")
        self.name_label.pack(pady=(10,5))

        self.name_input = tk.Entry(self)
        self.name_input.pack(pady=5)

        self.role_label = tk.Label(self, text="Employee Role")
        self.role_label.pack(pady=(10,5))

        self.role_input = tk.Entry(self)
        self.role_input.pack(pady=5)

        self.salary_label = tk.Label(self, text="Employee Salary")
        self.salary_label.pack(pady=(10,5))

        self.salary_input = tk.Entry(self)
        self.salary_input.pack(pady=5)


class ReadOneEmployeeWindow(TemplateWindow):
    def __init__(self,base):
        super().__init__(base)

class ReadAllEmployeeWindow(TemplateWindow):
    def __init__(self,base):
        super().__init__(base)

class UpdateEmployeeWindow(TemplateWindow):
   def __init__(self,base):
        super().__init__(base)

class DeleteEmployeeWindow(TemplateWindow):
    def __init__(self,base):
        super().__init__(base)

if __name__ == '__main__':
    janela = App()
    janela.mainloop()
