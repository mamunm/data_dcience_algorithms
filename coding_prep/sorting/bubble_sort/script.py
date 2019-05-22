#!/usr/bin/env python
# -*-coding: utf-8 -*-

#SCRIPT: script.py
#AUTHOR: Osman Mamun
#DATE CREATED: 05-22-2019

def bubble_sort(arr, reversed=False):
    swap_cnt = 0
    i = len(arr) - 1
    while i > 0:
        for j in range(i):
            if not reversed:
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swap_cnt += 1
            if reversed:
                if arr[j] < arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swap_cnt += 1
        i -= 1
    print('Number of swaps: {}'.format(swap_cnt))
    return arr

if __name__ == "__main__":
    print(bubble_sort([2, 4, 8, 5, 1, 9, 4]))
    print(bubble_sort([2, 4, 8, 5, 1, 9, 4], reversed=True))
