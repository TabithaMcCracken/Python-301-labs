# Write a decorator function that wraps text output into quotes, e.g.:
# Hello world! ----> "Hello World!"
# You can use it to create quotes from text output.

def decorator_func(initial_func):
    def wrapper_func(*args):
        print('"' + words + '"')
        return initial_func(*args)
    return wrapper_func

@decorator_func
def prettify(words):
    return words


words = "Hello World"
prettify(words)
