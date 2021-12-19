num = int(input("Enter a number: "))

table = [num*i for i in range(1,11)]

print(str(table))
with open('table.txt','a') as f:
    f.write(str(table))
    f.write('\n')