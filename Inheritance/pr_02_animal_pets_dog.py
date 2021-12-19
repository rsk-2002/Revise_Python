class Animals:
    animalsType = "Mammal"

class Pets(Animals):
    color = "white"

class Dog(Pets):
    @staticmethod
    def bark():
        print("Bow Bow")

d = Dog()
d.bark()