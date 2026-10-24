def check_time(func):
    def wrapper():
        print("Program started")
        func()
        print("Program ended")
    return wrapper

@check_time
def display():
    print("Displaying data")

display()