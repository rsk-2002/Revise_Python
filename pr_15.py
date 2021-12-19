sub1 = int(input("Enter your first subject marks: "))
sub2 = int(input("Enter your second subject marks: "))
sub3 = int(input("Enter your third subject marks: "))


if(sub1<33 or sub2<33 or sub3<33):
    print("you are fail coz you have less than 33\% \in one the subject")

elif(sub1+sub2+sub3)/3<40:
    print("you are fail due to total parcentage less than 40")

else:
    print("you are passed")