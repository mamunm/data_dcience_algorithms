#!/usr/bin/env python
# -*-coding: utf-8 -*-

#run_once_per_min.py
#Osman Mamun
#CREATED: 05-27-2019

from functools import wraps
from time import time, sleep

class CalledTooOftenError(Exception):
    pass

def once_per_minute(func):
    last_invoked = 0
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal last_invoked
        elapsed_time = time() - last_invoked
        if elapsed_time < 5:
            raise CalledTooOftenError(f'Only {elapsed_time} has passed.')
        last_invoked = time()
        return func(*args, **kwargs)
    return wrapper

@once_per_minute
def add(a, b):
    return a+b

if __name__ == "__main__":
    print(add(1, 2))
    try:
        print(add(4, 2))
    except CalledTooOftenError as e:
        print(e)
        sleep(6)
        print(add(4, 2))




