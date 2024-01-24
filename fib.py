#fib.py
from functools import lru_cache
import timer
memory = {}
def fib(n:int) -> int:
    if n <= 1:
        return n
    print(n)
    if n not in memory:
        memory[n] = fib(n-1) + fib(n-2)
    return memory[n]

if __name__ == "__main__":
    print(fib(100))
