#fib.py
from functools import lru_cache
import timer
import csv
memory = {}
def fib(n:int) -> int:
    t2 = timer.timer()
    t2._start('')
    if n <= 1:
        t2._stop('')
        print('Elapsed time for n =',n,':',t2._elapse * 1000, 'milliseconds')
        data = [int(n), float(t2._elapse) * 1000]
        writer.writerow(data)
        return n
        
    if n not in memory:
        memory[n] = fib(n-1) + fib(n-2)
    t2._stop('')
    print('Elapsed time for n =',n,':',t2._elapse * 1000, 'milliseconds')
    data = [int(n), float(t2._elapse) * 1000]
    writer.writerow(data)
    return memory[n]

if __name__ == "__main__":
    f = open('times.csv', 'w')
    writer = csv.writer(f)
    t = timer.timer()
    t._start('')
    print(fib(100))
    t._stop('')
    
    print('Total elapsed time:', t._elapse, 'seconds')
