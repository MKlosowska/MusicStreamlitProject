import time
from functools import wraps

# wypisuje czas wykonania funkcji w terminalu
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"[TIMER] {func.__name__} executed in {elapsed:.3f} s")
        return result
    return wrapper
