#models.py
class Employee():
    def __init__(self, name: str, role: str, salary: float, id: int = None):
        self.__id = id
        self.name = name
        self.role = role
        self.salary = salary
    
    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name
    
    @property
    def role(self):
        return self.__role
    
    @property
    def salary(self):
        return self.__salary
    
    @id.setter
    def id(self, new_id):
        if not isinstance(new_id, int):
            raise TypeError("ID must be an integer")
        self.__id = new_id

    
    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Name must be a string")
        self.__name = new_name
    
    @role.setter
    def role(self, new_role):
        if not isinstance(new_role, str):
            raise TypeError("Role must be a string")
        self.__role = new_role

    @salary.setter
    def salary(self, new_salary):
        if not isinstance(new_salary, float) and not isinstance(new_salary, int):
            raise TypeError("Salary must be a valid number")
        self.__salary = new_salary
    
