#Forms.py

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from .Styles import *
import Repository as repo



class AppWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Crud")
        
        self.geometry(WINDOW_SIZE)
        self.resizable(False, False)
        self.configure(bg=WINDOW_BG_COLOR)

        self.generate_widgets()

    def generate_widgets(self):
        self.title_label = tk.Label(self, text="Welcome to Simple Crud!", **APP_WINDOW_TITLE_STYLE)
        self.title_label.pack(**APP_WINDOW_TITLE_CONFIG)

        self.enter_button = tk.Button(self, text="Enter", **APP_WINDOW_BTN_STYLE, command= lambda: MainWindow(self))
        self.enter_button.pack(**APP_WINDOW_BTN_CONFIG)    

        self.exit_button = tk.Button(self, text="Exit", **APP_WINDOW_BTN_STYLE, command=self.destroy)
        self.exit_button.pack(**APP_WINDOW_BTN_CONFIG)

        self.autor_label = tk.Label(self, text="made by: Matheus Gana", **AUTOR_LABEL_STYLE)
        self.autor_label.pack(**AUTOR_LABEL_CONFIG)

class TemplateWindow(tk.Toplevel):
    def __init__(self, base):
        super().__init__(base)
        self.geometry(WINDOW_SIZE)
        self.configure(bg=WINDOW_BG_COLOR)

        #Model func to generete widgets
        self.generate_widgets()
        
        #Back Button
        tk.Button(self, text="Back", **BACK_BTN_STYLE,command=self.destroy).pack(side="bottom", pady=15)
        self.focus_force()
        self.grab_set()

class MainWindow(TemplateWindow):
    def __init__(self, base):
        super().__init__(base)

    def generate_widgets(self):
        self.title_label = tk.Label(self, text="Crud System", **MAIN_WINDOW_TITLE_STYLE)
        self.title_label.pack(**MAIN_WINDOW_TITLE_CONFIG)

        self.insert_button = tk.Button(self, text="Insert Employee", **MAIN_WINDOW_BTN_STYLE, command= lambda: InsertEmployeeWindow(self))
        self.insert_button.pack(**MAIN_WINDOW_BTN_CONFIG)

        self.read_one_employee_button = tk.Button(self, text="Read One Employee", **MAIN_WINDOW_BTN_STYLE, command= lambda: ReadOneEmployeeWindow(self))
        self.read_one_employee_button.pack(**MAIN_WINDOW_BTN_CONFIG)

        self.read_all_employees_button = tk.Button(self, text="Read All Employee", **MAIN_WINDOW_BTN_STYLE, command= lambda: ReadAllEmployeeWindow(self))
        self.read_all_employees_button.pack(**MAIN_WINDOW_BTN_CONFIG)

        self.update_employee_button = tk.Button(self, text="Update Employee", **MAIN_WINDOW_BTN_STYLE, command= lambda: UpdateEmployeeWindow(self))
        self.update_employee_button.pack(**MAIN_WINDOW_BTN_CONFIG)

        self.delete_employee_button = tk.Button(self, text="Delete Employee", **MAIN_WINDOW_BTN_STYLE, command= lambda: DeleteEmployeeWindow(self))
        self.delete_employee_button.pack(**MAIN_WINDOW_BTN_CONFIG)

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
        
        if status:
            print(f"Form Submitted: Name: {data['Name']}, Role: {data['Role']}, Salary: {data['Salary']}")
            tk.messagebox.showinfo("Success", result)
            self.focus_force()
        else:
            messagebox.showerror("Error", result)
            self.focus_force()

    
    def generate_widgets(self):
        self.title_label = tk.Label(self, text="Insert Employee", **MAIN_WINDOW_TITLE_STYLE)
        self.title_label.pack(**MAIN_WINDOW_TITLE_CONFIG)

        self.name_label = tk.Label(self, text="Employee Name", **MAIN_WINDOW_LABEL_STYLE)
        self.name_label.pack(**MAIN_WINDOW_LABEL_CONFIG)

        self.name_input = tk.Entry(self, **MAIN_WINDOW_INPUT_STYLE)
        self.name_input.pack(**MAIN_WINDOW_INPUT_CONFIG)

        self.role_label = tk.Label(self, text="Employee Role", **MAIN_WINDOW_LABEL_STYLE)
        self.role_label.pack(**MAIN_WINDOW_LABEL_CONFIG)

        self.role_input = tk.Entry(self, **MAIN_WINDOW_INPUT_STYLE)
        self.role_input.pack(**MAIN_WINDOW_INPUT_CONFIG)

        self.salary_label = tk.Label(self, text="Employee Salary", **MAIN_WINDOW_LABEL_STYLE)
        self.salary_label.pack(**MAIN_WINDOW_LABEL_CONFIG)

        self.salary_input = tk.Entry(self, **MAIN_WINDOW_INPUT_STYLE)
        self.salary_input.pack(**MAIN_WINDOW_INPUT_CONFIG)

        self.submit_btn = tk.Button(self, text="Submit", **SUBMIT_BTN_STYLE, command=self.submit_form)
        self.submit_btn.pack(**SUBMIT_BTN_CONFIG)

class ReadOneEmployeeWindow(TemplateWindow):
    def __init__(self,base):
        super().__init__(base)
    
    def submit_form(self):
        
        employee_id = self.id_input.get().strip()

        status, result = repo.get_employee(employee_id)

        if not status:
            messagebox.showerror("Database Error", result)
            self.destroy()
        elif not result:
            self.empty_employee_list_label = tk.Label(self, text="Employee table is empty", **RESULT_LABEL_STYLE)
            self.empty_employee_list_label.pack(**RESULT_LABEL_CONFIG)
        else:
            self.result_label = tk.Label(self, text=f"{result.name}, {result.role}, R${result.salary:.2f}", **RESULT_LABEL_STYLE)
            self.result_label.pack(**RESULT_LABEL_CONFIG)

    
    def generate_widgets(self):
        self.title_label = tk.Label(self, text="Read One Employee", **MAIN_WINDOW_TITLE_STYLE)
        self.title_label.pack(**MAIN_WINDOW_TITLE_CONFIG)

        self.id_label = tk.Label(self, text="Employee ID", **MAIN_WINDOW_LABEL_STYLE)
        self.id_label.pack(**MAIN_WINDOW_LABEL_CONFIG)

        self.id_input = tk.Entry(self, **MAIN_WINDOW_INPUT_STYLE)
        self.id_input.pack(**MAIN_WINDOW_INPUT_CONFIG)

        self.submit_btn = tk.Button(self, text="Submit", **SUBMIT_BTN_STYLE, command=self.submit_form)
        self.submit_btn.pack(**SUBMIT_BTN_CONFIG)

class ReadAllEmployeeWindow(TemplateWindow):
    def __init__(self,base):
        super().__init__(base)
    
    def generate_widgets(self):

        status, result = repo.get_all_employees()

        if not status:
            messagebox.showerror("Database Error", result)
            self.destroy()
        
        elif not result:
            messagebox.showwarning("Warning", "Database is empty!")
            self.destroy()

        else:
            self.title_label = tk.Label(self, text="Employee Table", **MAIN_WINDOW_TITLE_STYLE)
            self.title_label.pack(**MAIN_WINDOW_TITLE_CONFIG)

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
        messagebox.showinfo("Info", "Enter the employee ID you want to change," \
        " then enter the new information.")
        self.focus_force()
    
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
        self.title_label = tk.Label(self, text="Update Employee", **MAIN_WINDOW_TITLE_STYLE)
        self.title_label.pack(**MAIN_WINDOW_TITLE_CONFIG)

        self.id_label = tk.Label(self, text="Employee ID", **MAIN_WINDOW_LABEL_STYLE)
        self.id_label.pack(**MAIN_WINDOW_LABEL_CONFIG)

        self.id_input = tk.Entry(self, **MAIN_WINDOW_INPUT_STYLE)
        self.id_input.pack(**MAIN_WINDOW_INPUT_CONFIG)

        self.name_label = tk.Label(self, text="Employee Name", **MAIN_WINDOW_LABEL_STYLE)
        self.name_label.pack(**MAIN_WINDOW_LABEL_CONFIG)

        self.name_input = tk.Entry(self, **MAIN_WINDOW_INPUT_STYLE)
        self.name_input.pack(**MAIN_WINDOW_INPUT_CONFIG)

        self.role_label = tk.Label(self, text="Employee Role", **MAIN_WINDOW_LABEL_STYLE)
        self.role_label.pack(**MAIN_WINDOW_LABEL_CONFIG)

        self.role_input = tk.Entry(self, **MAIN_WINDOW_INPUT_STYLE)
        self.role_input.pack(**MAIN_WINDOW_INPUT_CONFIG)

        self.salary_label = tk.Label(self, text="Employee Salary", **MAIN_WINDOW_LABEL_STYLE)
        self.salary_label.pack(**MAIN_WINDOW_LABEL_CONFIG)

        self.salary_input = tk.Entry(self, **MAIN_WINDOW_INPUT_STYLE)
        self.salary_input.pack(**MAIN_WINDOW_INPUT_CONFIG)

        self.submit_btn = tk.Button(self, text="Submit", **SUBMIT_BTN_STYLE, command=self.submit_form)
        self.submit_btn.pack(**SUBMIT_BTN_CONFIG)

class DeleteEmployeeWindow(TemplateWindow):
    def __init__(self,base):
        super().__init__(base)

    def submit_form(self):
         
        employee_id = self.id_input.get().strip()

        status, result = repo.delete_employee(employee_id)
        
        if status:
            tk.messagebox.showinfo("Success", result)
            self.focus_force()
        else:
            messagebox.showerror("Error", result)
            self.destroy()
    
    def generate_widgets(self):
        self.title_label = tk.Label(self, text="Delete Employee", **MAIN_WINDOW_TITLE_STYLE)
        self.title_label.pack(**MAIN_WINDOW_TITLE_CONFIG)

        self.id_label = tk.Label(self, text="Employee ID", **MAIN_WINDOW_LABEL_STYLE)
        self.id_label.pack(**MAIN_WINDOW_LABEL_CONFIG)

        self.id_input = tk.Entry(self, **MAIN_WINDOW_INPUT_STYLE)
        self.id_input.pack(**MAIN_WINDOW_INPUT_CONFIG)

        self.submit_btn = tk.Button(self, text="Submit", **SUBMIT_BTN_STYLE, command=self.submit_form)
        self.submit_btn.pack(**SUBMIT_BTN_CONFIG)
