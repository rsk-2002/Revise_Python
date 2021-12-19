words = ['donkey','kaddu','mote','pagal']
with open("sample.txt") as f:
    text = f.read()
    
for word in words:
    text = text.replace(word, '$$%^^$$#')
with open("sample.txt",'w') as f:
    f.write(text)