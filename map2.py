def square(x):
    return x ** 2

l = [2, 4, 6, 8]
newl = []

for item in l:
    newl.append(square(item))

print(newl)