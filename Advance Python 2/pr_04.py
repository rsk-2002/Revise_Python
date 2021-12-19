# def divided_by_5(num):
#     if num%5==0:
#         return True
#     else:
#         return False
l1 = [2,5,10,34,20]

# print(list(filter(divided_by_5, l1)))
print(list(filter(lambda a:a%5==0, l1)))
