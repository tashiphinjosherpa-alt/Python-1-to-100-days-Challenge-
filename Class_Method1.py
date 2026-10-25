class Employee:
    company = "Microsoft"

    @classmethod
    def changeCompany(cls, new_company):
        cls.company = new_company

Employee.changeCompany("Google")

print(Employee.company)