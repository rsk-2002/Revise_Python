class Employee:
    company = "Google"
    salary = 100

harry = Employee()
rajni = Employee()

# Creating instance attribute salary for both objects
# harry.salary = 300
# rajni.salary = 400
harry.salary = 45
print(harry.salary)
print(rajni.salary)
# print(rajni.address) # Throws an error as address in not present in instance/class