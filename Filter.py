def filter_function(a):
    return a > 2

l = [3, 4, 1, 23, 234]

newl = list(filter(filter_function, l))
print(newl)