
# factorial = 0

# def factorial_iter(n):
#     product = 1
#     for i in range(n):
#         product = product * (i+1)
#     return product

# f = factorial_iter(5)
# print(f)

def factorial_recursive(n):
    if n==1 or n==0:
        return 1
    return n* factorial_recursive(n-1) #recursion here

f = factorial_recursive(1)
print(f)

