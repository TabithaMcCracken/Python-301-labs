#Write a decorator function that wraps text passed to it in a specified HTML tag. 
# The user should be able to decide which tag to use.
# OUTPUT: <p>Hello, Bessy</p>

def tagify(*tag):
    def inner_func(func):
        def wrapper(*args):
            text = func(*args)
            result = f"<{tag[0]}>{text}<{tag[0]}>"
            return result
        return wrapper
    return inner_func


@tagify("div")
def greet(name):
    return f"Hello, {name}"

print(greet("Bessy"))  