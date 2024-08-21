class Employee:

    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1 

    @classmethod
    def print_employee_count(cls):
        print(f"Загальна кількість співробітників: {cls.employee_count}")

    def print_employee_info(self):
        print(f"Ім'я: {self.name}, Зарплата: {self.salary}")

emp1 = Employee("Олександр", 5000)
emp2 = Employee("Марина", 6000)

emp1.print_employee_info()  
emp2.print_employee_info() 

Employee.print_employee_count() 

print(f"Базові класи: {Employee.__bases__}")
print(f"Простір імен класу: {Employee.__dict__}")
print(f"Назва класу: {Employee.__name__}")
print(f"Назва модуля: {Employee.__module__}")
print(f"Документація класу: {Employee.__doc__}")
