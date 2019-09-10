#!/usr/bin/env python
# -*-coding: utf-8 -*-

#SCRIPT: script.py
#AUTHOR: Osman Mamun
#DATE CREATED: 07-08-2019

import pytest

def sum_a_b(a, b):
    return a + b

@pytest.mark.parametrize('a, b, r', [(3, 4, 7), (-3, 3, 0), (0, 5, 5)])
def test_sum_a_b(a, b, r):
    assert sum_a_b(a, b) == r
