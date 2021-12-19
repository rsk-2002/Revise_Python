content = True
lineNumber = 1
with open('log.txt') as f:
    while content:
        content = f.readline()
        if 'python' in content.lower():
            print(content)
            print("Yes python is present on line Number",lineNumber)
        lineNumber+=1