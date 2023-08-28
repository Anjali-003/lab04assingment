class Employee:
    def __init__(self, employee_id, name, age, salary):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeDatabase:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def print_employees(self):
        for employee in self.employees:
            print(f"Employee ID: {employee.employee_id}, Name: {employee.name}, Age: {employee.age}, Salary: {employee.salary}")

    def sort_employees(self, key):
        if key == 1:  # Sort by Age
            self.employees.sort(key=lambda x: x.age)
        elif key == 2:  # Sort by Name
            self.employees.sort(key=lambda x: x.name)
        elif key == 3:  # Sort by Salary
            self.employees.sort(key=lambda x: x.salary)
        else:
            print("Invalid sorting parameter")

if __name__ == "__main__":
    db = EmployeeDatabase()

    db.add_employee(Employee("161E90", "Raman", 41, 56000))
    db.add_employee(Employee("161F91", "Himadri", 38, 67500))
    db.add_employee(Employee("161F99", "Jaya", 51, 82100))
    db.add_employee(Employee("171E20", "Tejas", 30, 55000))
    db.add_employee(Employee("171G30", "Ajay", 45, 44000))

    sorting_option = int(input("Choose sorting parameter (1. Age, 2. Name, 3. Salary): "))
    db.sort_employees(sorting_option)

    db.print_employees()
