class Student:
    def __init__(self):
        self._name = "Tashi"   

    def _display(self):        
        print("Protected Method")

class College(Student):
    def show(self):
        print(self._name)      
        self._display()

obj = College()
obj.show()