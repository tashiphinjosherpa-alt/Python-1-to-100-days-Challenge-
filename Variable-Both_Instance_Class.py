class Employee:
    company = "Microsoft"  

    def __init__(self, name):
        self.name = name   

e1 = Employee("Tashi")
e2 = Employee("Ram")

print(e1.name)
print(e2.name)

print(e1.company)
print(e2.company)