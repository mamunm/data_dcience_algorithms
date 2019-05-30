#!/usr/bin/env python
# -*-coding: utf-8 -*-

#script.py
#Osman Mamun
#CREATED: 05-28-2019


def get_sub(arr): #O(N*N)
    max_sum = None
    max_list = None
    for i in range(0, len(arr)):
        j = i
        while j < len(arr):
            j += 1
            temp_list = arr[i:j]
            temp_sum = sum(temp_list)
            if max_sum == None:
                max_list = temp_list
                max_sum = temp_sum
            else:
                if temp_sum > max_sum:
                    max_list = temp_list
                    max_sum = temp_sum
    return max_list, max_sum

def max_sub(arr): #O(N)
    if arr is None or len(arr) == 0:
        return 0
    summed = 0
    n = len(arr)
    solutions = [0] * n
    for ind, value in enumerate(arr):
        if summed < 0:
            summed = 0
        summed += value
        solutions[ind] = summed
    return max(solutions)



if __name__ == "__main__":
    print(get_sub([-2, -3, 4, -1, -2, 1, 5, -3]))
    print(max_sub([-2, -3, 4, -1, -2, 1, 5, -3]))
