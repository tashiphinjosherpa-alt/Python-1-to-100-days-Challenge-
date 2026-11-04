def multiply(x):

    def inner(y):
        return x * y

    return inner

double = multiply(2)

print(double(5))