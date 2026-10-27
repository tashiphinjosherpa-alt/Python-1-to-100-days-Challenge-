class Employee:
    def __init__(self, name):
        self.name = name
        print("Employee Constructor")

class Programmer(Employee):
    def __init__(self, name):
        super().__init__(name)
        print("Programmer Constructor")

obj = Programmer("Tashi")