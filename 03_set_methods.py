b = set()

print(type(b))

# adding value to an empty set 

b.add(4)
b.add(5)
b.add(5)

# cannot add list and dictionary in sets 
# b.add([2,4,5]) #list cannot
b.add((2,4,5)) #tuple can

# print(len(b)) # prints the length of this set

# b.remove(5)
print(b.pop())
print(b)