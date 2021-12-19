with open('poems.txt','r') as f:
    a = f.read()
    if 'twinklew' in a:
        print("Exist")
    else:
        print("not Exist")
