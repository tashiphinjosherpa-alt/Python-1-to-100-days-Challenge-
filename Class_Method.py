class Student:
    school = "Dwit School"

    @classmethod
    def showSchool(cls):
        print(cls.school)

Student.showSchool()