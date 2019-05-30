#!/usr/bin/env python
# -*-coding: utf-8 -*-

#SCRIPT: return_to_origin.py
#AUTHOR: Osman Mamun
#DATE CREATED: 05-29-2019

def judge_circle(moves):
    a = {'RL': 0, 'UD': 0}
    for m in moves:
        if m == 'R':
            a['RL'] += 1
        elif m == 'L':
            a['RL'] -= 1
        elif m == 'U':
            a['UD'] += 1
        else:
            a['UD'] -= 1
    if a['UD'] == 0 and a['RL'] == 0:
        return True
    else:
        return False

print(judge_circle('UD'))
print(judge_circle('UDLR'))
print(judge_circle('UDUUDDLLRLRRR'))
print(judge_circle('UUUUDDDDDDD'))
