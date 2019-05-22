#!/usr/bin/env python
# -*-coding: utf-8 -*-

#SCRIPT: script.py
#AUTHOR: Osman Mamun
#DATE CREATED: 05-22-2019

class Node:
    def __init__(self, val):
        self.right = None
        self.left = None
        self.val = val

    def insert(self, val):
        if self.val:
            if val < self.val:
                if self.left is  None:
                    self.left = Node(val)
                else:
                    self.left.insert(val)
            if val > self.val:
                if self.right is None:
                    self.right = Node(val)
                else:
                    self.right.insert(val)
        else: 
            self.val = val
    
    def search(self, val):
        if self.val == val:
            return '{} is found!'.format(val)
        else:
            if self.val < val:
                if self.right is None:
                    return '{} is not found!'.format(val)
                else:
                    return self.right.search(val)
            if self.val > val:
                if self.left is None:
                    return '{} is not found!'.format(val)
                else:
                    return self.left.search(val)

r = Node(30)
r.insert(20)
r.insert(10)
r.insert(3)
r.insert(8)
r.insert(24)
r.insert(80)
r.insert(5)

print(r.search(8))
print(r.search(4))
    

