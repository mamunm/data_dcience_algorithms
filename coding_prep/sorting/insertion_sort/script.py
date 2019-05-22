#!/usr/bin/env python
# -*-coding: utf-8 -*-

#SCRIPT: script.py
#AUTHOR: Osman Mamun
#DATE CREATED: 05-22-2019

def insertion_sort(arr):
    for i in range(1, len(arr)):
        k = arr[i]
        for j in range(i, 0, -1):
            if arr[j-1] > k:
                arr[j-1], arr[j] = arr[j], arr[j-1]
    return arr

def insertion_sort_reversed(arr):
    for i in range(1, len(arr)):
        k = arr[i]
        for j in range(i, 0, -1):
            if arr[j-1] < k:
                arr[j-1], arr[j] = arr[j], arr[j-1]
    return arr

if __name__ == "__main__":
    print(insertion_sort([2, 5, 8, 1, 9, 4]))
    print(insertion_sort_reversed([2, 5, 8, 1, 9, 4]))


