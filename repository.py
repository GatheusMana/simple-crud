#repository.py
from models import Employee
from database import connection, cursor


def create_employee(employee_obj) -> bool:
    cursor.execute("INSERT INTO employees (name, role, salary) VALUES (?, ?, ?)", 
                    (employee_obj.name, employee_obj.role, employee_obj.salary))
    
    connection.commit()
    return cursor.rowcount > 0
    

def get_employee(id) -> Employee:
    employee_data = cursor.execute("SELECT * FROM employees WHERE id = ?", (id,)).fetchone()
    if not employee_data:
        return None
    _, *employee = employee_data
    return Employee(*employee, id)


def get_all_employees() -> list:
    employee_table = cursor.execute("SELECT * FROM employees").fetchall()
    employee_list = []

    for row in employee_table:
        id, *employee_data = row
        employee_list.append(Employee(*employee_data, id))

    return employee_list

def update_employee(name, role, salary, id) -> bool:
    cursor.execute("UPDATE employees SET name = ?, role = ?, salary = ? WHERE id = ?",
                  (name, role, salary, id))
        
    connection.commit()
    return cursor.rowcount > 0

def delete_employee(employee_id) -> bool:
    cursor.execute("DELETE FROM employees WHERE id = ?", (employee_id,))
    connection.commit()
    
    return cursor.rowcount > 0