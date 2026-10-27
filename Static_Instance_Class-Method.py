class Demo:
    x = 100

    def instance_method(self):
        print("Instance Method")

    @classmethod
    def class_method(cls):
        print("Class Method")

    @staticmethod
    def static_method():
        print("Static Method")

obj = Demo()

obj.instance_method()
Demo.class_method()
Demo.static_method()