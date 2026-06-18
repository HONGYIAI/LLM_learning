# The first case is for python decorator
import time

from functools import wraps

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Time taken: {time.time() - start} seconds")
        return result
    return wrapper
    
def slow_function() = timer(slow_function)
slow_function