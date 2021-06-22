import functools


def memoize(function):
    function._cache = {}

    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        k = (args, tuple(kwargs.items()))
        if k not in function._cache:
            function._cache[k] = function(*args, **kwargs)
        return function._cache[k]

    return wrapper


"""
def memoize(function):
    cache = {}
    
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        k = (args, tuple(kwargs.items()))
        if k not in cache:
            cache[k] = function(*args, **kwargs)
        return cache[k] 
    
    return wrapper
"""