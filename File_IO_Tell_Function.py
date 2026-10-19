with open("MyFile4.txt", "r") as f:
    data = f.read(5)
    print(data)
    print(f.tell())