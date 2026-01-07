#repository.py
from Models import Employee
from DatabaseManager import DatabaseManager


def add_employee(employee_obj) -> tuple:
    try:
        with DatabaseManager("data.db") as cursor:
            cursor.execute("INSERT INTO employees (name, role, salary) VALUES (?, ?, ?)", 
                    (employee_obj.name, employee_obj.role, employee_obj.salary))
    
            return (True, f"Success! Welcome {employee_obj.name}")
    except Exception as e:
        return (False, f"Repository error: {e}")

def get_employee(str_id) -> tuple:
    try:
        id = int(str_id)

        with DatabaseManager("data.db") as cursor:
            employee_data = cursor.execute("SELECT * FROM employees WHERE id = ?", (id,)).fetchone()
            if not employee_data:
                return (True, None)
            emp_id, name, role, salary = employee_data
            return (True, Employee(name, role, salary, emp_id))
    
    except ValueError as e:
        return (False, f"ID must be a integer number")
    except Exception as e:
        return (False, f"Repository error: {e}")
        

def get_all_employees() -> tuple:
    try:
        with DatabaseManager("data.db") as cursor:
            employee_table = cursor.execute("SELECT * FROM employees").fetchall()
            employee_list = []

            for row in employee_table:
                id, *employee_data = row
                employee_list.append(Employee(*employee_data, id))

            return (True, employee_list)
    
    except Exception as e:
        return (False, f"Repository error: {e}")

def update_employee(name, role, salary, id) -> bool:
    try:
        with DatabaseManager("data.db") as cursor:
            cursor.execute("UPDATE employees SET name = ?, role = ?, salary = ? WHERE id = ?",
                            (name, role, salary, id))    
            return (True, "Success")
    except Exception as e:
        return(False, f"Repository error: {e}")

def delete_employee(employee_id) -> bool:
    try:
        with DatabaseManager("data.db") as cursor:
            cursor.execute("DELETE FROM employees WHERE id = ?", (employee_id,))
            return (True, "Success")
    except Exception as e:
        return (False, f"Repository error: {e}")