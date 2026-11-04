def outer():

    msg = "Hello"

    def inner():
        print(msg)

    return inner

func = outer()
func()