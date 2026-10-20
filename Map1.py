def cube(x):
    return x ** 3

l = [3, 4, 1, 23, 234]
newl = []

for item in l:
    newl.append(cube(item))

print(newl)