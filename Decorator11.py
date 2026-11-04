def decorator(func):
    def wrapper():
        print("Before")

        func()

        print("After")

    return wrapper


@decorator
def greet():
    print("Hello my name is Tashi Phinjo Sherpa")


greet()