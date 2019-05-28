#!/usr/bin/env python
# -*-coding: utf-8 -*-

#memoization.py
#Osman Mamun
#CREATED: 05-27-2019

from functools import wraps

def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        if args not in cache:
            print("Caching new function value for {}({})".format(
                func.__name__, args))
            cache[args] = func(*args, **kwargs)
        else:
            print("Using old value from the cache for {}({})".format(
            func.__name__, args))
        return cache[args]
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return 1
    else:
        return n * fibonacci(n-1)


print(fibonacci(20))
print(fibonacci(10))
print(fibonacci(5))
print(fibonacci(20))
print(fibonacci(10))
