class Employee:
    company = "Bharat Gas"
    salary = 4600
    salaryBonus = 510
    # totalSalary = 5100

    @property
    def totalSalary(self):
        return self.salary + self.salaryBonus

    @totalSalary.setter
    def totalSalary(self,val):
        self.salaryBonus = val - self.salary
e = Employee()
print(e.salaryBonus)
print(e.totalSalary)
e.totalSalary = 5500
print(e.salary)
print(e.salaryBonus)