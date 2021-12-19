myDict = {
    "fast":"In a quick manner",
    "ravi":"a Coder",
    "marks":[1,3,4,6],
    "anotherDict":{"name":"priya","age":23},
    1:34
}

# dictionary methods 
# print(list(myDict.keys()))
# print(myDict.values())

# print(myDict)

updateDict = {
    "Lovish":"Friend",
    "Ratan":"Friend",
    "Ria":"Friend",
    "ravi":"a dancer",
}

myDict.update(updateDict)

# both give same value 
print(myDict.get('ravi')) 
print(myDict['ravi']) 

print(myDict.get('ravi2')) # print None
print(myDict['ravi2']) # throw an error
# print(myDict)