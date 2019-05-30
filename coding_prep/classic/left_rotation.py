#!/usr/bin/env python
# -*-coding: utf-8 -*-

#SCRIPT: left_rotation.py
#AUTHOR: Osman Mamun
#DATE CREATED: 05-29-2019

def rot_left(a, d):
    return a[d:] + a[:d]

print(rot_left([1, 2, 3, 4, 5], 4))
