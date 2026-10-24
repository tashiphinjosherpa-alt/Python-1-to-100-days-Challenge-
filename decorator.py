def add_sprinkle(fun):
    def wrapper():
        print("You add a sprinkle")
        fun()
    return wrapper

@add_sprinkle
def get_Ice_cream():
    print("Here is your ice cream")

get_Ice_cream()