class Person:
    def show_name(self):
        print("Name: Tashi")

class Student(Person):
    def show_roll(self):
        print("Roll No: 101")

class Monitor(Student):
    def show_section(self):
        print("Section: A")

m = Monitor()

m.show_name()
m.show_roll()
m.show_section()