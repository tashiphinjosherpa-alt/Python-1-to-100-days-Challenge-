class Student:
    def __init__(self, name):
        self.__name = name   

    
    def get_name(self):
        return self.__name

    
    def set_name(self, name):
        self.__name = name

s = Student("Tashi")

print(s.get_name())  

s.set_name("Sherpa") 

print(s.get_name())