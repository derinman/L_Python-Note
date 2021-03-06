import concurrent.futures

FIBS = [28, 10, 20, 20, 23, 30, 10, 30]

def fib(n):
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)

#ThreadPoolExecutor適合IO密集
#ProcessPoolExecutor適合CPU密集

def process():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, fib_value in zip(FIBS, executor.map(fib, FIBS)):
            print("%d's fib number is %d" % (number, fib_value))

if __name__ == '__main__':
    process()