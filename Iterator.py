numbers=[12,45,78,00,77,45]
it=iter(numbers)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))



print()



it = iter(numbers)

for x in it:
    print(x)