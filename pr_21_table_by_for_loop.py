num = int(input("Enter the number: "))

# for i in range(1,11):
#     print(str(num),'X',str(i),'=',num*i)
#     i+=1


# table using while loop
# i = 1
# while(i<11):
#     print(str(num),'X',str(i),'=',num*i)
#     i+=1

# reverse order table 
for i in range(-10,0):
    print(str(num),'X',i-(i*2),'=',num*i-(num*i*2))
    i+=1