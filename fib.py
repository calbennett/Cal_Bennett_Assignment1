#fib.py
from functools import lru_cache
import timer
def fib(n:int) -> int:
    if n <= 1:
        return n
    else:
        return fib(n-2) + fib(n-1)

if __name__ == "__main__":
    fib(5)