class Employee:
    def salary(self):
        print("Base Salary")

class Programmer(Employee):
    def salary(self):
        print("Salary = 50000")

class Manager(Employee):
    def salary(self):
        print("Salary = 80000")

employees = [Programmer(), Manager()]

for emp in employees:
    emp.salary()
