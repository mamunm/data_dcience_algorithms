#!/usr/bin/env python
# -*-coding: utf-8 -*-

#SCRIPT: merge_sort.py
#AUTHOR: Osman Mamun
#DATE CREATED: 06-02-2019

def merge(A, B):
    def insert(m):
        for i in range(len(A)):
            if A[i] < m:
                continue
            else:
                A.insert(i, m)
                break
    for b in B:
        if b > A[-1]:
            A.append(b)
        else:
            insert(b)
    return A

def merge_sort(A):
    if len(A) == 1:
        return A
    if len(A) == 2:
        if A[0] < A[1]:
            return A
        else: 
            return A[::-1]
    while True:
        low = 0
        high = len(A) - 1
        mid = (low + high) // 2
        m = merge_sort(A[:mid+1])
        n = merge_sort(A[mid+1:])
        return merge(m, n)
        


if __name__ == "__main__":
    print(merge_sort([2, 5, 1, 7, 8, 4]))


