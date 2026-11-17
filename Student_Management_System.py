class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

    def result(self):
        if self.marks >= 40:
            print("Pass")
        else:
            print("Fail")

s1 = Student("Tashi", 75)

s1.display()
s1.result()