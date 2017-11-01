from functools import wraps

def print_function_name(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print('Call: {}'.format(f.__name__))
        return f(*args, **kwargs)
    return wrapper

@print_function_name
def square(x):
    return x * x

print(square(3) + square(4))
#|Call: square
#|Call: square
#|25
