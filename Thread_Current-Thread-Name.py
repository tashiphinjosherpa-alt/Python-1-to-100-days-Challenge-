import threading

def task():
    print(threading.current_thread().name)
    

t = threading.Thread(target=task)

t.start()