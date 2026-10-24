def add_sprinkle(fun):
    def wrapper(flavor):
        print("You add sprinkle here")
        fun(flavor)
    return wrapper

def add_fudge(fun):
    def wrapper(flavor):
        print("You add fudge")
        fun(flavor)
    return wrapper

@add_sprinkle
@add_fudge
def get_Ice_cream(flavor):
    print(f"Here is your {flavor} ice cream")

get_Ice_cream("Vanilla")