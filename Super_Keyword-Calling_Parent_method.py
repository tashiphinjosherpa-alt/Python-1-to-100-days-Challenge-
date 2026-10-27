class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def awaj(self):
        super().sound()
        print("Dog barks")

d = Dog()
d.awaj()