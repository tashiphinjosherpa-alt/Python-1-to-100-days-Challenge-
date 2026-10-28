from functools import cache

@cache
def factorial(n):
    print(f"Calculating factorial({n})")
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
print(factorial(5))