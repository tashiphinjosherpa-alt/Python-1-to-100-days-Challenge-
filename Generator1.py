def demo():
    yield "Hello"
    yield "Tashi"

g = demo()

print(next(g))
print(next(g))