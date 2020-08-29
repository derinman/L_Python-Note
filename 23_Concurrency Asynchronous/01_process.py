import threading

#用terminal執行
def do_this (what):
    whoami (what)

def whoami (what):
    print("Thread {} says: {}".format(threading.current_thread(), what))

if __name__ == "__main__":
    for i in range(4):
        p = threading.Thread( target= do_this, args = ("I'm function{}".format(i),) )
        p.start()
