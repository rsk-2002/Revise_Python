class Person:
    country = "India"

    def takeBreathe(self):
        print("I am breathing...")

class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreathe(self):
        print("I am an Employee so I am breathing...")

class Programmer(Employee):
    company = "Fiverr"

    def getSalary(self):
        print("No salary to programmer")

    def takeBreathe(self):
        print("I am an Programmer so I am breathing++...")

p = Person()
p.takeBreathe()
e = Employee()
e.takeBreathe()
pr = Programmer()
pr.takeBreathe()
print(pr.country)