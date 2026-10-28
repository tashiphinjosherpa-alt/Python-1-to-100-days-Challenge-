import threading
import time

def task():
    time.sleep(2)
    print("Task Complete")

t = threading.Thread(target=task)

t.start()

t.join()

print("Program End")