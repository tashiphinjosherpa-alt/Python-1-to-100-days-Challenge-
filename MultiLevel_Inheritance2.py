class A:
    def __init__(self):
        print("Class A")

class B(A):
    def __init__(self):
        super().__init__()
        print("Class B")

class C(B):
    def __init__(self):
        super().__init__()
        print("Class C")

obj = C()