def square(n):
    return n*n
l = [1,2,4]

# Method 1 
# l2 = []
# for item in l:
#     l2.append(square(item))

# Method 2 Map 
print(list(map(square, l)))

