def readFile(name):
    try:
        with open(name) as f:
            print(f.read())
    except FileNotFoundError:
        print(f"file {name} is not found")
readFile('1.txt')
readFile('3.txt')
readFile('2.txt')