class Student:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):      
        return self.__name

    @name.setter
    def name(self, value):   
        self.__name = value

s = Student("Tashi")

print(s.name)

s.name = "Phinjo"

print(s.name)