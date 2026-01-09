#Repository.py
from Models import Employee
from DatabaseManager import DatabaseManager

class RequiredFieldsError(Exception):
    """Raised when required fields are empty"""
    pass

def database_is_empty():
    try:
         with DatabaseManager("data.db") as cursor:
            count = cursor.execute("SELECT COUNT(*) FROM employees").fetchone()[0]
            return count == 0
    
    except Exception as e:
        return (False, f"Repository error: {e}")

def add_employee(name, role, salary) -> tuple:
    try:

        if not all([name, role, salary]):
            raise RequiredFieldsError("All fields are required!")
        employee_obj = Employee(name, role, float(salary))

        with DatabaseManager("data.db") as cursor:
            cursor.execute("INSERT INTO employees (name, role, salary) VALUES (?, ?, ?)", 
                    (employee_obj.name, employee_obj.role, employee_obj.salary))
            
            return (True, f"Success! Welcome {employee_obj.name}!")
    
    except RequiredFieldsError as e:
        return (False, f"Input Error: {e}")
    except TypeError as e:
        return (False, f"Input Error: {e}")
    except ValueError as e:
        return (False, f"Input Error: {e}")
    except Exception as e:
        return (False, f"Repository error: {e}")

def get_employee(str_id) -> tuple:
    if database_is_empty():
        return (True, None)
    try:
        id = int(str_id)

        with DatabaseManager("data.db") as cursor:
            employee_data = cursor.execute("SELECT * FROM employees WHERE id = ?", (id,)).fetchone()
            emp_id, name, role, salary = employee_data
            return (True, Employee(name, role, salary, emp_id))
    
    except ValueError as e:
        return (False, f"ID must be a integer number!")
    except Exception as e:
        return (False, f"Repository error: {e}")
        

def get_all_employees() -> tuple:
    if database_is_empty():
        return (True, None)
    
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
    if database_is_empty():
        return (False, "Database is empty")
    
    try:
        if not all([name, role, salary, id]):
            raise RequiredFieldsError("All fields are required!")

        new_employee = Employee(name=name,role=role,salary=float(salary),id=id)

        with DatabaseManager("data.db") as cursor:
            cursor.execute("UPDATE employees SET name = ?, role = ?, salary = ? WHERE id = ?",
                            (new_employee.name, new_employee.role, new_employee.salary, new_employee.id))    
            
            return (True, f"Success! New data for Employee {new_employee.id}!")
    except RequiredFieldsError as e:
        return (False, f"Input Error: {e}")
    except TypeError as e:
        return (False, f"Input Error: {e}")
    except ValueError as e:
        return (False, f"Input Error: {e}")
    except Exception as e:
        return (False, f"Repository error: {e}")


def delete_employee(employee_id) -> bool:
    if database_is_empty():
        return (False, "Database is empty")
    try:
        with DatabaseManager("data.db") as cursor:
            cursor.execute("DELETE FROM employees WHERE id = ?", (employee_id,))
            return (True, f"Employee {employee_id} was deleted successfully!")
    except Exception as e:
        return (False, f"Repository error: {e}")