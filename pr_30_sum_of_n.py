def sum_recursive(n):
    if n==1 or n==0:
        return 1
    return n+ sum_recursive(n-1) #recursion here



ans = sum_recursive(1)
print(ans)