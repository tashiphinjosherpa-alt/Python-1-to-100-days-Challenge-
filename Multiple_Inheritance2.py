class Teacher:
    def teach(self):
        print("Teaching students")

class Writer:
    def write(self):
        print("Writing books")

class Professor(Teacher, Writer):
    pass

p = Professor()

p.teach()
p.write()