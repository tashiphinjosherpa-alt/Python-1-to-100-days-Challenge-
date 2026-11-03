class Employee:
    def __init__(self):
        self.__salary = 0

    def setSalary(self, salary):
        self.__salary = salary

    def getSalary(self):
        return self.__salary

e = Employee()

e.setSalary(50000)

print(e.getSalary())