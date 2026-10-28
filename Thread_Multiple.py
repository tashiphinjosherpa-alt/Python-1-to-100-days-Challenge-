import threading

def show():
    print("Running")

t1 = threading.Thread(target=show)
t2 = threading.Thread(target=show)
t3 = threading.Thread(target=show)

t1.start()
t2.start()
t3.start()

print("Program is end")