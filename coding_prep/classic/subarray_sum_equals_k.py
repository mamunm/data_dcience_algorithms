#!/usr/bin/env python
# -*-coding: utf-8 -*-

#SCRIPT: subarray_sum_equals_k.py
#AUTHOR: Osman Mamun
#DATE CREATED: 05-29-2019

from collections import defaultdict
def subarray_sum(nums, k):
    cnt = 0
    sums = 0
    hash_dict = {}
    hash_dict[0] = 1
    for i in range(len(nums)):
        sums += nums[i]
        if (sums - k) in hash_dict:
            cnt += hash_dict[sums-k]
        if sums in hash_dict:
            hash_dict[sums] += 1
        else:
            hash_dict[sums] = 1
    return cnt

if __name__ == "__main__":
   print(subarray_sum([10, 2, -2, -20, -10], -10))
   print(subarray_sum([1, 1, 1], 2))
   print(subarray_sum([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0))
