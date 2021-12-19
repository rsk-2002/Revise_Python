with open("sample.txt") as f:
    text = f.read()
    if 'donkey' in text:
        text = text.replace('donkey', '######')
with open("sample.txt",'w') as f:
    f.write(text)