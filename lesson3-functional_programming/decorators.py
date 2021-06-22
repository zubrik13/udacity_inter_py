# timer decorator
import functools
import time
import timeit


def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        value = func(*args, **kwargs)
        start_time = time.perf_counter()    # 1
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer


@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])


def time_it(fn):
    return timeit.timeit(lambda: fn, number=10000)


def time_rep(fn):
    return timeit.repeat(lambda: fn, repeat=6, number=10000)


# debug code
def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # 4
        return value
    return wrapper_debug


@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"

if __name__ == "__main__":
    waste_some_time(1)
    waste_some_time(998)

    # canonical way by timeit module
    fn = sum([i**2 for i in range(10000)])
    print(time_it(fn))
    print(time_rep(fn))

    make_greeting("Roman")
    make_greeting("Mark", age=43)