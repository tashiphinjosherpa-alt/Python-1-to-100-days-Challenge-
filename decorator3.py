def decorator_function(func):
    def wrapper(name):
        print("Welcome!")
        func(name)
        print("Goodbye!")
    return wrapper

@decorator_function
def greet(name):
    print("Hello", name)

greet("Tashi")