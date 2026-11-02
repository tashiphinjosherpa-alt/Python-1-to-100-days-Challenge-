class Employee:
    def work(self):
        print("Employee Working")

class Programmer(Employee):
    def work(self):
        print("Writing Code")

class Manager(Employee):
    def work(self):
        print("Managing Team")

e1 = Programmer()
e2 = Manager()

e1.work()
e2.work()