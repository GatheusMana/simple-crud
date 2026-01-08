#Forms.py

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from .Styles import *
import Repository as repo
import Models as models



class AppWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Crud")
        
        self.geometry(window_geometry_size)
        self.resizable(False, False)

        self.generate_widgets()

    def generate_widgets(self):
        self.welcome_label = tk.Label(self, text="Welcome to Simple Crud!", font=(title_font_style))
        self.welcome_label.pack(pady=20, expand=True)

        self.enter_button = tk.Button(self, text="Enter", width=enter_window['BUTTON_WIDTH'], command= lambda: MainWindow(self))
        self.enter_button.pack(pady=enter_window['BUTTON_PADY'])    

        self.exit_button = tk.Button(self, text="Exit", width=enter_window['BUTTON_WIDTH'], command=self.destroy)
        self.exit_button.pack(pady=enter_window['BUTTON_PADY'])


        self.autor_label = tk.Label(self, text="made by: Matheus Gana", font=(autor_font_style))
        self.autor_label.pack(pady=50)

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
        self.insert_button.pack(pady=(30,5), expand=True)

        self.read_one_employee_button = tk.Button(self, text="Read One Employee", width=template_window['BUTTON_WIDTH'], command= lambda: ReadOneEmployeeWindow(self))
        self.read_one_employee_button.pack(pady=template_window['BUTTON_PADY'], expand=True)

        self.read_all_employees_button = tk.Button(self, text="Read All Employee", width=template_window['BUTTON_WIDTH'], command= lambda: ReadAllEmployeeWindow(self))
        self.read_all_employees_button.pack(pady=template_window['BUTTON_PADY'], expand=True)

        self.update_employee_button = tk.Button(self, text="Update Employee", width=template_window['BUTTON_WIDTH'], command= lambda: UpdateEmployeeWindow(self))
        self.update_employee_button.pack(pady=template_window['BUTTON_PADY'], expand=True)

        self.delete_employee_button = tk.Button(self, text="Delete Employee", width=template_window['BUTTON_WIDTH'], command= lambda: DeleteEmployeeWindow(self))
        self.delete_employee_button.pack(pady=template_window['BUTTON_PADY'], expand=True)

class InsertEmployeeWindow(TemplateWindow):
    def __init__(self,base):
        super().__init__(base)

    def submit_form(self):

        data = {
            "Name": self.name_input.get().strip(),
            "Role": self.role_input.get().strip(),
            "Salary": self.salary_input.get().strip()
        }    
        
        status, result = repo.add_employee(data['Name'], data['Role'], data['Salary'])

        print(f"Form Submitted: Name: {data['Name']}, Role: {data['Role']}, Salary: {data['Salary']}")
        
        if status:
            tk.messagebox.showinfo("Success", result)
        else:
            messagebox.showerror("Error", result)

    
    def generate_widgets(self):
        self.title("Insert Employee")

        self.name_label = tk.Label(self, text="Employee Name")
        self.name_label.pack(pady=(10,5), expand=True)

        self.name_input = tk.Entry(self)
        self.name_input.pack(pady=5, expand=True)

        self.role_label = tk.Label(self, text="Employee Role")
        self.role_label.pack(pady=(10,5), expand=True)

        self.role_input = tk.Entry(self)
        self.role_input.pack(pady=5, expand=True)

        self.salary_label = tk.Label(self, text="Employee Salary")
        self.salary_label.pack(pady=(10,5), expand=True)

        self.salary_input = tk.Entry(self)
        self.salary_input.pack(pady=5, expand=True)

        self.submit_btn = tk.Button(self, text="Submit", command=self.submit_form)
        self.submit_btn.pack(pady=5, expand=True)

class ReadOneEmployeeWindow(TemplateWindow):
    def __init__(self,base):
        super().__init__(base)
    
    def submit_form(self):
        
        employee_id = self.id_input.get().strip()

        status, result = repo.get_employee(employee_id)

        if not status:
            messagebox.showerror("Database Error", result)

        elif not result:
            self.empty_employee_list_label = tk.Label(self, text="Employee table is empty", font=("Arial", 14,"bold"))
            self.empty_employee_list_label.pack(pady=50)
        else:
            self.result_label = tk.Label(self, text=f"{result.name}, {result.role}, R${result.salary:.2f}", font=("Arial", 14,"bold"))
            self.result_label.pack(pady=50)

    
    def generate_widgets(self):
        self.title("Read One Employee")

        self.title_label = tk.Label(self, text="Read One Employee", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=20)

        self.id_label = tk.Label(self, text="Employee ID")
        self.id_label.pack(pady=(10,5))

        self.id_input = tk.Entry(self)
        self.id_input.pack(pady=5)

        self.submit_btn = tk.Button(self, text="Submit", command=self.submit_form)
        self.submit_btn.pack(pady=5)

class ReadAllEmployeeWindow(TemplateWindow):
    def __init__(self,base):
        super().__init__(base)
    
    def generate_widgets(self):
        self.title("Read All Employees")

        status, result = repo.get_all_employees()

        if not status:
            messagebox.showerror("Database Error", result)
        
        elif not result:
            self.empty_employee_list_label = tk.Label(self, text="Employee table is empty", font=("Arial", 14,"bold"))
            self.empty_employee_list_label.pack(pady=50)
        
        else:
            self.title_label = tk.Label(self, text="Employee Table", font=("Arial", 16, "bold"))
            self.title_label.pack(pady=20)

            self.employee_table_frame = tk.Frame(self)
            self.employee_table_frame.pack(pady=10)

            self.employee_table_tree = ttk.Treeview(self.employee_table_frame, columns=('id', 'name', 'role', 'salary'), show='headings', height=10)
            self.employee_table_tree.heading('id', text='ID')
            self.employee_table_tree.heading('name', text='Name')
            self.employee_table_tree.heading('role', text='Role')
            self.employee_table_tree.heading('salary', text='Salary')
            
            self.employee_table_tree.column('id', width=50, anchor='center')
            self.employee_table_tree.column('name', width=250, anchor='w')
            self.employee_table_tree.column('role', width=150, anchor='w')
            self.employee_table_tree.column('salary', width=100, anchor='w')

            self.employee_table_scrollbar = tk.Scrollbar(self.employee_table_frame, orient=tk.VERTICAL, command=self.employee_table_tree.yview)
            self.employee_table_tree.configure(yscroll=self.employee_table_scrollbar.set)

            self.employee_table_tree.pack(side=tk.LEFT)
            self.employee_table_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            
            for employee in result:
                self.employee_table_tree.insert('', tk.END, values=(employee.id,employee.name,employee.role, employee.salary))

class UpdateEmployeeWindow(TemplateWindow):
    def __init__(self,base):
        super().__init__(base)
    
    def submit_form(self):
        data = {
            "ID" : self.id_input.get().strip(),
            "Name": self.name_input.get().strip(),
            "Role": self.role_input.get().strip(),
            "Salary": self.salary_input.get().strip()
        }    
        
        status, result = repo.update_employee(data['Name'], data['Role'], data['Salary'], data["ID"])

        print(f"Form Submitted: Name: {data['Name']}, Role: {data['Role']}, Salary: {data['Salary']} for Employee: {data["ID"]}")
        
        if status:
            tk.messagebox.showinfo("Success", result)
        else:
            messagebox.showerror("Error", result)

    def generate_widgets(self):
        self.title("Update Employee")

        self.title_label = tk.Label(self, text="Update Employee", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=20)

        self.id_label = tk.Label(self, text="Employee ID")
        self.id_label.pack(pady=(10,5))

        self.id_input = tk.Entry(self)
        self.id_input.pack(pady=5)

        self.name_label = tk.Label(self, text="Employee Name")
        self.name_label.pack(pady=(10,5), expand=True)

        self.name_input = tk.Entry(self)
        self.name_input.pack(pady=5, expand=True)

        self.role_label = tk.Label(self, text="Employee Role")
        self.role_label.pack(pady=(10,5), expand=True)

        self.role_input = tk.Entry(self)
        self.role_input.pack(pady=5, expand=True)

        self.salary_label = tk.Label(self, text="Employee Salary")
        self.salary_label.pack(pady=(10,5), expand=True)

        self.salary_input = tk.Entry(self)
        self.salary_input.pack(pady=5, expand=True)

        self.submit_btn = tk.Button(self, text="Submit", command=self.submit_form)
        self.submit_btn.pack(pady=5, expand=True)

class DeleteEmployeeWindow(TemplateWindow):
    def __init__(self,base):
        super().__init__(base)

    def submit_form(self):
         
        employee_id = self.id_input.get().strip()

        status, result = repo.delete_employee(employee_id)
        
        if status:
            tk.messagebox.showinfo("Success", result)
        else:
            messagebox.showerror("Error", result)
    
    def generate_widgets(self):
        self.title("Delete Employee")

        self.title_label = tk.Label(self, text="Delete Employee", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=20)

        self.id_label = tk.Label(self, text="Employee ID")
        self.id_label.pack(pady=(10,5))

        self.id_input = tk.Entry(self)
        self.id_input.pack(pady=5)

        self.submit_btn = tk.Button(self, text="Submit", command=self.submit_form)
        self.submit_btn.pack(pady=5)
