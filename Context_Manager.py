# without context manager
file = open("file.txt")

data = file.read()

file.close()

# with Context manager
with open("file.txt") as file:
    print(file.read())