class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(self.name, self.salary)

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def manager_info(self):
        print(self.name)
        print(self.salary)
        print(self.department)

m1 = Manager("Ali", 5000, "IT")

m1.show()
m1.manager_info()
