# Build on top of the censorship exercise and change your decorator function
# so that you can pass the words it should censor when decorating a function, e.g.:
# `@censor("shoot", "crab")` would censor the words "shoot" and "crab".


def censor(*words):
    def inner_function(func):
        def wrapper(*args, **kwargs):
            output = func(*args, **kwargs)
            for word in words:
                output = output.replace(word, '*' * len(word))
            return output
        return wrapper
    return inner_function

@censor("shoot", "crab")
def my_func(text):
    return text

print(my_func("I like to shoot crabs."))





# def decorator_func(initial_func):
#     def wrapper_func(*args, *kwargs):
#         if *args in text:
