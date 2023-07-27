# Create a decorator that censors potentially offensive words from a text.
# For example, assuming that "shoot" was considered an offensive word:
# A function that would normall return this text:
#    "I bumped my toe! Shoot!"
# Would, after decorating it with `@censor()`, return:
#    "I bumped my toe! S****!"

def decorator_func(initial_func):
    def wrapper_func(*args):
        if "Shoot" in text:
            print(text.replace("Shoot", "S****"))
        return initial_func(*args)
    return wrapper_func

@decorator_func
def print_text(text):
    return text

text = "I bumped my toe! Shoot"   
print_text(text)