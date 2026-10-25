class Student:
    def __init__(self):
        self.__name = "Tashi"   

    def display(self):
        print(self.__name)

obj = Student()
obj.display()

# print(obj.__name) Error