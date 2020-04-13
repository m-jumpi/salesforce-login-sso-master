from time import perf_counter


def counter(fn):
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print('{0} was called {1} times'.format(fn.__name__, count))
        return fn(*args, **kwargs)

    return inner


@counter
def add(a, b):
    return a + b


add(10, 20)

