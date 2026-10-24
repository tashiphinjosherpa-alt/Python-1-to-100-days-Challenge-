class Student:
    def __init__(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

s = Student(20)

print("Age:", s.get_age())

s.set_age(21)

print("New Age:", s.get_age())