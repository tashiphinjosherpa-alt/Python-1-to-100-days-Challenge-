class Employee:
    company = "Microsoft"

    def __init__(self, name):
        self.name = name

Employee.company = "Google"

e1 = Employee("Tashi")
e2 = Employee("Ram")

print(e1.company)
print(e2.company)