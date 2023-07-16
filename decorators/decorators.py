"""
    useful decorators
"""

import time

def log(func):

    def wrapper(*args, **kwargs):
        s = time.perf_counter()
        result = func(*args, **kwargs)
        e = time.perf_counter()
        print(f"{func.__name__} -> {result} in {e - s:0.4f}s")
        return result
    
    return wrapper