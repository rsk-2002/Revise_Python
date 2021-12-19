a = [3,4,5,67,87,122,109]

# b = []
# for item in a:
#     if item%2 == 0:
#         b.append(item)

# print(b)
# Shortcut to write the same
b = [i for i in a if i%2==0]
print(b)

t = [1,4,3,1,2,3]
s = {i for i in t}
print(s)