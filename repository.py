#repository.py
from models import Employee
from database import connection, cursor


def save_employee(employee_obj):
    cursor.execute("INSERT INTO employees (name, role, salary) VALUES (?, ?, ?)", 
                    (employee_obj.name, employee_obj.role, employee_obj.salary))
    connection.commit()
    

def get_all_employees() -> list:
    employee_table = cursor.execute("SELECT * FROM employees").fetchall()
    employee_list = []

    for row in employee_table:
        id, *employee_data = row
        employee_list.append(Employee(*employee_data, id))

    return employee_list