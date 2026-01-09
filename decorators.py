import time
from functools import wraps

def timer(func):
    """Dekorator: mierzy czas wykonania funkcji."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"[timer] {func.__name__}: {time.time() - start:.2f}s")
        return result
    return wrapper
