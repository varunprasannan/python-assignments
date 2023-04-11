import functools
import time


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()  # start timer
        main = func(*args, **kwargs)  # run function
        end = time.perf_counter()  # end timer
        elapsed = end - start  # calculate elapsed time
        print(f"Elapsed time: {elapsed:0.4f} seconds")
        return main
    return wrapper


@timer
def normal_function():
    for i in range(10000000):
        i * 5


normal_function()

# Output:
# Elapsed time: 0.3339 seconds
