class Vector:
    def __init__(self,vec):
        self.vec = vec

    def __str__(self):
        return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"

    def __len__(self):
        return len(self.vec)

v1 = Vector([1,4,6,7])
v2 = Vector([1,6,9])
print(len(v1))
print(len(v2))
# print(v2)ṇ