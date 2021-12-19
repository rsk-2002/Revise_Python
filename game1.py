import random

def gameWin(comp,you):
    if comp==you:
        return None
    if(comp=='s' and you=='g'):
        return True
    elif(comp=='w' and you =='s'):
        return True
    elif(comp=='g' and you=='w'):
        return True
    else:
        return False


a = print("Computer Turn: Snake(s),water(w) or gun(g)?")
randNo = random.randint(0,2)
choiceList = ['s','w','g']
comp = choiceList[randNo]
# print(comp)

you = input("Your's Turn: Snake(s),water(w) or gun(g)?")

a = gameWin(comp,you)

print(f"Computer chose {comp} and you chose {you}")
if a==None:
    print("The game is a tie!")
elif a:
    print("Congrats, You Won!")
else:
    print("You lose.")