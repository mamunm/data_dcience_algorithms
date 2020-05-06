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

@timed
@memoize
def fibonacci(n):
    if n < 2:
        return 1
    else:
        return n * fibonacci(n-1)


print('Fibonacci number for n = 20 is {}.'.format(fibonacci(20)))
print('Fibonacci number for n = 10 is {}.'.format(fibonacci(20)))
