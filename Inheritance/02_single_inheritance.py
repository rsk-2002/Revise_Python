class Employee:
    company = "Google"

    def showDetails(self):
        print("This is an Employee")

class Programmer(Employee):
    language = "Python"
    company = "YouTube"

    def getLang(self):
        print(f"THe language is {self.language}")

    def showDetails(self):
        print("This is a Programmer")

e = Employee()
e.showDetails()
p = Programmer()
p.showDetails()
print(p.company)