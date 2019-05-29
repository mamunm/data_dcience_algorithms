#!/usr/bin/env python
# -*-coding: utf-8 -*-

#SCRIPT: fizz_buzz.py
#AUTHOR: Osman Mamun
#DATE CREATED: 05-29-2019

for i in range(100):
    if i % 3 == 0:
        st = 'Fizz'
        if i % 5 == 0:
            st += 'Buzz'
    elif i % 5 == 0:
        st = 'Buzz'
    else:
        st = str(i)
    print(st)
