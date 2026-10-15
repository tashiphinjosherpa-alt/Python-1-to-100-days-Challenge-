Colors=["Red", "Yellow","Purple","Green","Pink"]
print(Colors)
print(Colors.index("Green"))


num=[2,1,4,2,6,2,2,7,9]
print(num.index(6))

print(num.count(2))

mum=num
mum[0]=0
print(num)

Colors.insert(2,"White")
print(Colors)

mum=[100,900,600,345]
num.extend(mum)
print(num)