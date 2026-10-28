import threading

def hello():
    print("Hello from thread")

t = threading.Thread(target=hello)

t.start()