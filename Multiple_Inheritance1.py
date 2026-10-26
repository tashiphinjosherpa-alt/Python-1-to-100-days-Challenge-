class Camera:
    def click(self):
        print("Taking photo")

class Phone:
    def call(self):
        print("Making call")

class Smartphone(Camera, Phone):
    pass

s = Smartphone()

s.click()
s.call()
