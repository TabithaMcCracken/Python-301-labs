# Create a custom decorator function that records the execution time of
# the decorated function and prints the time to your console when the function
# has finished execution.
import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        run_time = end_time - start_time
        print(f"Finished the function in {run_time: .3f} seconds.")
        return result
    return wrapper

@time_it
def my_function(x):
    return sum(i**2 for i in range(x))

my_function(1000000)