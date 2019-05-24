#!/usr/bin/env python
# -*-coding: utf-8 -*-

#SCRIPT: script.py
#AUTHOR: Osman Mamun
#DATE CREATED: 05-22-2019

def selection_sort(arr, reversed=False):
    for i in range(len(arr)):
        ind = i
        val = arr[i]
        for j in range(i+1, len(arr)):
            if not reversed:
                if arr[j] < val:
                    val, ind = arr[j], j
            if reversed:
                if arr[j] > val:
                    val, ind = arr[j], j
        arr[i], arr[ind] = arr[ind], arr[i]
    return arr


if __name__ == "__main__":
    print(selection_sort([2, 5, 8, 1, 9, 4]))
    print(selection_sort([2, 5, 8, 1, 9, 4], reversed=True))


