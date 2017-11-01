from datetime import datetime
import functools

def track_time(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = f(*args, **kwargs)
        print('Run {}: {}'.format(f.__name__, datetime.now() - start))
        return result
    return wrapper

@track_time
def bad_sum(n):
    s, i = 0, 0
    while i <= n:
        s += i
        i += 1
    return s

@track_time
def good_sum(n):
    return sum(range(n + 1))

n = 10 ** 6
print(good_sum(n) == bad_sum(n))
#|Run good_sum: 0:00:00.327170
#|Run bad_sum: 0:00:00.874342
#|True
