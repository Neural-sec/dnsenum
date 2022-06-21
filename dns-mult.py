from queue import Queue
import queue
import threading, socket

domain = "exemplo.com"
lock = threading.Lock()

def brute_force():
    while not q.empty():
        DNS = q.get() + "." + domain
        try:
            IP = socket.gethostbyname(DNS)
            lock.acquire()
            print(DNS + ":\t" + IP)
        except socket.gaierror:
                pass
        else:
            lock.release()
        q.task_done()
    q = queue()
    for i in range(20):
        t = threading.Thread(target=brute_force)
        t.daemon = True
        t.start()
    with open("list.txt") as list:
        while True:
            name = list.readline().strip("\n")
            if not name:
                break
            q.put(name)
        q.join()
        print("\nMapeamento Completo")