#!/usr/bin/env python
# -*-coding: utf-8 -*-

#SCRIPT: script.py
#AUTHOR: Osman Mamun
#DATE CREATED: 06-01-2019

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, val):
        self.head = Node(val)

    def insert(self, val):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(val)
        
    def print_list(self):
        out = []
        cur_node = self.head
        while cur_node.next != None:
            out += [cur_node.val]
            cur_node = cur_node.next
        out += [cur_node.val]
        print(out)

    def __len__(self):
        l = 0
        cur = self.head
        while cur.next != None:
            l += 1
            cur = cur.next
        l += 1
        return l

    def __getitem__(self, ind):
        if not 0<=ind<=len(self):
            print('ERROR: index out of bound')
            return
        idx = 0
        cur = self.head
        while idx != ind:
            cur = cur.next
            idx += 1
        return cur.val

    def remove(self, ind):
        if not 0<=ind<=len(self):
            print('ERROR: index out of bound')
            return
        idx = 0
        cur = self.head
        while True:
            last_node = cur
            cur = cur.next
            if idx == ind-1:
                last_node.next = cur.next
                return
            idx += 1


if __name__ == "__main__":
    ll = LinkedList(0)
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    ll.print_list()
    print(len(ll))
    print(ll[0])
    print(ll[3])
    print(ll[20])
    ll.remove(1)
    ll.print_list()


