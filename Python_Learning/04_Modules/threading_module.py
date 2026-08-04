import threading
import time

def task():
    for i in range(5):
        print("Running...", i)
        time.sleep(1)

thread = threading.Thread(target=task)

thread.start()

thread.join()

print("Thread Finished")