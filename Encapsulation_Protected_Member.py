class Student:
    def __init__(self, name):
        self._name = name

class Child(Student):
    def show(self):
        print(self._name)

s = Child("Tashi")
s.show()

print(s._name)