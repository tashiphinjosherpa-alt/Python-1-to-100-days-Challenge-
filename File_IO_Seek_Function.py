with open('MyFile4.txt', 'r') as f:
    f.seek(10)
    data = f.read(12)
    print(data)