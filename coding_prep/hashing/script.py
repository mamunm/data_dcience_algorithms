#!/usr/bin/env python
# -*-coding: utf-8 -*-

#SCRIPT: script.py
#AUTHOR: Osman Mamun
#DATE CREATED: 05-23-2019

class hash:
    def __init__(self, size):
        self.size = size
        self.key = [None] * size
        self.value = [None] * size
    
    def get_hash_val(self, val, size):
        return val % size

    
