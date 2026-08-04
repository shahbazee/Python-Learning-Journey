from multiprocessing import Process
import os

def worker():
    print("Process ID:", os.getpid())

if __name__ == "__main__":
    process = Process(target=worker)

    process.start()
    process.join()

    print("Main Process Finished")