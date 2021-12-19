myDict = {
    'pankha':'fan',
    'dabba':'box',
    'vastu':'item'
}

print("Options are ",myDict.keys())
a = input('Enter the Hindi word\n')
print("The meaning of your word is",myDict.get(a))
# print("The meaning of your word is",myDict[a])  #throws an error if key is not available 