def my_generatora():
    for i in range(5):
        yield i

gen = my_generatora()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))