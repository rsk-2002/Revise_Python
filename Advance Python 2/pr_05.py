from functools import reduce

l = [3,5,11,8]

a = reduce(max, l)

print(a)