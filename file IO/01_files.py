

f = open('sample.txt','r')
# f = open('sample.txt') # by default the mode is r

data = f.read()
# data = f.read(4) #first 4 character


print(data)
f.close()