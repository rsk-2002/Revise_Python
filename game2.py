import random 
randNumber = random.randint(1, 100)
print(randNumber)
number = None
guesses = 0

while number!=randNumber:
    number = int(input("Enter the number: "))
    guesses +=1
    if number == randNumber:
        print("You got the number",number)
    else:
        if number>randNumber:
            print("Enter a smaller number: ")
        else:
            print("Enter a larger number: ")
with open('hiscore.txt') as f:
    score = int(f.read())

if score>guesses:
    print(f"You took {guesses} guesses to find the number and you break hiscore")
    with open('hiscore.txt','w') as f:
        f.write(str(guesses))

    