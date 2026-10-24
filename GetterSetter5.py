class Marks:
    def __init__(self):
        self.__marks = 0

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Marks should be between 0 and 100")

m = Marks()

m.set_marks(85)

print(m.get_marks())