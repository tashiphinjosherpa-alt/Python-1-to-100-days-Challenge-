def count():
    yield 1
    yield 2
    yield 3

gen = count()

print(next(gen))
print(next(gen))
print(next(gen))