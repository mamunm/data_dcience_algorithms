#!/usr/bin/env python
# -*-coding: utf-8 -*-

#script.py
#Osman Mamun
#CREATED: 05-20-2019

def get_sub(M, N):
    for i, a in enumerate(M):
        for j, b in enumerate(N):
            if a == b:
                return a + get_sub(M[i+1:], N[j+1:])
    return ''

def long_sub(A, B):
    temp = []
    for i, a in enumerate(A):
        temp += [get_sub(A[i:], B)]
    if temp:
        return max(temp, key=len)
    else:
        return ''

if __name__ == '__main__':
    print(long_sub('ABAZDC', 'BACBAD'))
    print(long_sub('AGGTAB', 'GXTXAYB'))
    print(long_sub('aaaaa', 'aa'))
    print(long_sub('', '...'))
    print(long_sub('ABBA', 'ABCABA'))
