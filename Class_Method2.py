class Employee:
    company = "Microsoft"

    def __init__(self, name):
        self.name = name

    @classmethod
    def changeCompany(cls, company_name):
        cls.company = company_name

e1 = Employee("Tashi")
e2 = Employee("Ram")

print(e1.company)
print(e2.company)

Employee.changeCompany("Google")

print(e1.company)
print(e2.company)