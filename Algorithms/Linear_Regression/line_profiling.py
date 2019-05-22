#!/usr/bin/env python
# -*-coding: utf-8 -*-

import unittest
from lin_reg import LinearRegression
import numpy as np

@profile
def test_predict():
    X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
    y = np.dot(X, np.array([1, 2])) + 3
    lr = LinearRegression()
    lr.fit(X, y)
    y_pred = lr.predict(np.array([[3, 5], [4, 5], [2, 4]]))

if __name__ == '__main__':
    test_predict()

'''line_profiling: 1. kernprof -l line_profiling.py
                   2. python -m line_profiler line_profiling.py.lprof
'''
