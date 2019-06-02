#!/usr/bin/env python
# -*-coding: utf-8 -*-

#SCRIPT: script.py
#AUTHOR: Osman Mamun
#DATE CREATED: 06-02-2019

class MinHeap:
    def __init__(self, lst):
        self.heap = []

        for l in lst:
            self.heap.append(l)
            self._bubble_up(len(self.heap)-1)

    def push(self, val):
        self.heap.append(val)
        self._bubble_up(len(self.heap) - 1)

    def peek(self):
        if self.heap:
            return self.heap[0]

    def pop(self):
        if not self.heap:
            return 'Heap empty.'
        if len(self.heap) == 1:
            return self.heap.pop()
        self._swap(0, -1)
        rval = self.heap.pop()
        self._bubble_down(0)
        return rval 

    def _swap(self, a, b):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]

    def _bubble_up(self, index):
        parent = index // 2
        if self.heap[parent] > self.heap[index]:
            self._swap(parent, index)
            self._bubble_up(parent)
    
    def _bubble_down(self, index):
        smallest = index
        child_1 = index * 2 + 1
        child_2 = index * 2 + 2

        if child_1+1 <= len(self.heap): 
            if self.heap[child_1] < self.heap[index]:
                smallest = child_1
        if child_2+1 <= len(self.heap):
            if self.heap[child_2] < self.heap[index]:
                smallest = child_2
        if smallest != index:
            self._swap(smallest, index)
            self._bubble_down(smallest)

    def print_heap(self):
        print(self.heap)

if __name__ == "__main__":
    m = MinHeap([20, 25, 21, 10, 34, 8, 3, 11])
    m.print_heap()
    print(m.peek())
    print(m.pop())
    m.print_heap()
    m.push(1)
    m.push(7)
    m.push(39)
    m.print_heap()

