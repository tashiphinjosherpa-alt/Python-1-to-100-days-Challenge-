def is_even(num):
    return num % 2 == 0

l = [1, 2, 3, 4, 5, 6, 7, 8]

newl = list(filter(is_even, l))

print(newl)