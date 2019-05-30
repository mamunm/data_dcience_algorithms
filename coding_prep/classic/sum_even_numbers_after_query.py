#!/usr/bin/env python
# -*-coding: utf-8 -*-

#SCRIPT: sum_even_numbers_after_query.py
#AUTHOR: Osman Mamun
#DATE CREATED: 05-29-2019

def sum_even_after_queries(A, queries):
    out = []
    even_sum = sum(i for i in A if i%2==0)
    for q in queries:
        if A[q[1]] % 2 == 0:
            even_sum -= A[q[1]]
        A[q[1]] += q[0]
        if A[q[1]] % 2 == 0:
            even_sum += A[q[1]]
        out += [even_sum]
    return out

print(sum_even_after_queries([1, 2, 3, 4], 
      [[1, 0], [-3, 1], [-4, 0], [2, 3]]))
