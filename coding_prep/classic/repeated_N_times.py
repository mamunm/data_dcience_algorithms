#!/usr/bin/env python
# -*-coding: utf-8 -*-

#SCRIPT: repeated_N_times.py
#AUTHOR: Osman Mamun
#DATE CREATED: 05-29-2019

from collections import Counter

def repeated_N_times(A):
    N = len(A) / 2
    m = Counter(A)
    for k in m:
        if m[k] == N:
            return k

print(repeated_N_times([1, 2, 3, 3]))
