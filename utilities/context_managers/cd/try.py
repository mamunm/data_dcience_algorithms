#!/usr/bin/env python
# -*-coding: utf-8 -*-
import os
from script import CD, cd

print(os.listdir())

with CD('/Users/osmanmamun/Play_Ground'):
    print(os.listdir())

print(os.listdir())

with cd('/Users/osmanmamun/Play_Ground'):
    print(os.listdir())

print(os.listdir())

