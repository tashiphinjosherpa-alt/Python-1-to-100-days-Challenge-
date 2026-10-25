class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetail(self):
        print(f"The name of employee {self.id} is {self.name}")


class Programmer(Employee):
    def showLanguage(self):
        print("The default language is Python")


e = Employee("Tashi", 123)
e.showDetail()
e1=Programmer("Hari Bahadur",234)

e1.showLanguage()