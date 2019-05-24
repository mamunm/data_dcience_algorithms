#!/usr/bin/env python
# -*-coding: utf-8 -*-

#script.py
#Osman Mamun
#CREATED: 05-20-2019

def get_long(A):
    from itertools import groupby
    A = [ord(i) for i in A]
    g = [list(v) for k, v in groupby(enumerate(A), key=lambda i: i[0]-i[1])]
    g = max(g, key=len)
    return ''.join([chr(i[1]) for i in g])


if __name__ == '__main__':
    print(get_long('abcmnopqrxyz'))
