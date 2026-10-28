import threading

def task():
    print("Child Thread")

t = threading.Thread(target=task)

t.start()

print("Main Thread")
