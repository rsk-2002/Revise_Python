letter = '''Dear <|name|>,
You are selected!

Date <|Date|>
'''
name = input("Enter your name\n")
date = input("Enter date\n")
letter = letter.replace("<|name|>", name)
letter = letter.replace("<|Date|>", date)
print(letter)