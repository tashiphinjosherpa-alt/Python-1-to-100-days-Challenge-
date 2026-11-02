class Bird:
    def move(self):
        print("Flying")

class Fish:
    def move(self):
        print("Swimming")

def action(obj):
    obj.move()

action(Bird())
action(Fish())