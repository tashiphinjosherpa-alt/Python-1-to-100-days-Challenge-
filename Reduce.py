from functools import reduce

numbers = [2, 45, 1, 27]

total = reduce(lambda x, y: x + y, numbers)

print(total)