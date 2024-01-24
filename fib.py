#fib.py
from functools import lru_cache
import timer
memory = {}
def fib(n:int) -> int:
    if n <= 1:
        return n
    if n not in memory:
        memory[n] = fib(n-1) + fib(n-2)
    return memory[n]

if __name__ == "__main__":
    t = timer.timer()
    t._start('Starting...')
    print(fib(100))
    t._stop('Done')
    
    print(t._elapse)
