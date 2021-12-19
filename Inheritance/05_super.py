class Person:
    country = "India"

    def __init__(self):
        print("Initializing Person...\n")

    def takeBreathe(self):
        print("I am breathing...")

class Employee(Person):
    company = "Honda"

    def __init__(self):
        super().__init__()
        print("Initializing Employee...\n")    

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreathe(self):
        super().takeBreathe()
        print("I am an Employee so I am breathing...")

class Programmer(Employee):
    company = "Fiverr"

    def __init__(self):
        # super().__init__()
        print("Initializing Programmer...\n") 

    def getSalary(self):
        print("No salary to programmer")

    def takeBreathe(self):
        super().takeBreathe()
        print("I am an Programmer so I am breathing++...")

# p = Person()
# p.takeBreathe()

# e = Employee()
# e.takeBreathe()

pr = Programmer()
# pr.takeBreathe()