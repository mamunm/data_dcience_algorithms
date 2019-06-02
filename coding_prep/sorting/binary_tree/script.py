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


def print_tree(tree):
    if tree.left == None and tree.right == None:
        print('Node(val = {}, left=None, right=None)'.format(tree.val))
    if tree.right != None and tree.left == None:
        print('Node(val = {}, left = None, right={})'.format(tree.val, 
            tree.right.val))
        print_tree(tree.right)
    if tree.left != None and tree.right == None:
        print('Node(val = {}, left = {}, right=None)'.format(tree.val, 
            tree.left.val))
        print_tree(tree.left)
    if tree.left != None and tree.right != None:
        print('Node(val = {}, left = {}, right={})'.format(tree.val, 
            tree.left.val, tree.right.val))
        print_tree(tree.left)
        print_tree(tree.right)


def tree_height(tree):
    if tree == None:
        return 0
    if tree.left == None and tree.right == None:
        return 1
    return max(tree_height(tree.left), tree_height(tree.right)) + 1

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
print('Height of the tree: {}'.format(tree_height(r)))
print('\n')
print_tree(r)
    

