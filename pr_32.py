def remove_and_split(string,word):
    newStr = string.replace(word,"")
    return newStr.strip()

this = "    Ravi is a good boy  "
n = remove_and_split(this, "Ravi")
print(n)
# print(this)

# print(this.strip())