# 07_spinner_thread.py 與 08_spinner_asyncio.py 分別展示
# 使用執行緒編寫並行(concurrent)與使用協同程序編寫並行

# spinner_thread.py

# credits: Adapted from Michele Simionato's
# multiprocessing example in the python-list:
# https://mail.python.org/pipermail/python-list/2009-February/538048.html

# BEGIN SPINNER_THREAD
import threading
import itertools
import time


def spin(msg, done):  #這個函式執行一個獨立的執行緒，扮演第二個執行緒
    for char in itertools.cycle('|/-\\'):  #迭代無窮迴圈
        status = char + ' ' + msg
        print(status, flush=True, end='\r')
        if done.wait(.1):
            break
    print(' ' * len(status), end='\r')

def slow_function():  #這個函式執行另一個執行緒，並且阻塞主執行緒
    # pretend waiting a long time for I/O
    time.sleep(3)  # <8>
    return 42


def supervisor():
    done = threading.Event()
    spinner = threading.Thread(target=spin,args=('thinking!', done))
    print('spinner object:', spinner)
    spinner.start()  #開始第二個執行緒
    result = slow_function()  #阻塞主執行緒3秒
    done.set()  
    spinner.join()
    return result


def main():
    result = supervisor()
    print('Answer:', result)


if __name__ == '__main__':
    main()
# END SPINNER_THREAD