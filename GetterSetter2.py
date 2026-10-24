class Employee:
    def __init__(self):
        self.__salary = 0

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            print("Salary cannot be negative")
        else:
            self.__salary = value

e = Employee()

e.salary = 30000
print(e.salary)

e.salary = -5000