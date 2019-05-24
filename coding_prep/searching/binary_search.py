#!/usr/bin/env python
# -*-coding: utf-8 -*-

#SCRIPT: script.py
#AUTHOR: Osman Mamun
#DATE CREATED: 05-23-2019

def search_binary(arr, val):
    low, high = 0, len(arr) - 1
    midpoint = len(arr) // 2
    
    while low <= high:
        midpoint = (low + high) // 2
        if arr[midpoint] == val:
            return val
        elif arr[midpoint] > val:
            high = midpoint - 1
        elif arr[midpoint] < val:
            low = midpoint + 1 
    return 'val not found!'

if __name__ == "__main__":
    print(search_binary([1, 3, 5, 6, 7, 8, 9], 4))
    print(search_binary([1, 3, 5, 6, 7, 8, 9], 5))
    print(search_binary([1, 3, 5, 6, 7, 8, 9], -4))
    print(search_binary([1, 3, 5, 6, 7, 8, 9], 11))
    print(search_binary([1, 3, 5, 6, 7, 8, 9], 8))
