class Math:
    def add(self, *args):
        print(sum(args))

m = Math()

m.add(10, 20)
m.add(10, 20, 30)
m.add(10, 20, 30, 40)
