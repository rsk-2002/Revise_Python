class Calculator:
    def __init__(self,num):
        self.number = num

    def square(self):
        print(f"Square of {self.number} is {self.number**2}")

    def squareRoot(self):
        print(f"Square Root of {self.number} is {self.number**(1/2)}")
        
    def cube(self):
        print(f"Cube of {self.number} is {self.number**3}")

a = Calculator(9)
a.square()
a.squareRoot()
a.cube()
