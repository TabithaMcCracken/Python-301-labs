# Write a decorator that literally decorates text output.
# Make it so the symbol it uses can be an argument to the decorator
#
# The output of a function that returns `"Hello"` that has been
# decorated like with `@decorate("*")` should look like this:
#
# ******************************
# Hello
# ******************************

def decorator_func(initial_func):
    def wrapper_func():
        result = initial_func()
        line = "*" * 5
        return f"{line}\n{result}\n{line}"
    return wrapper_func



@decorator_func
def pretty_word():
    return "Hello"

print(pretty_word())