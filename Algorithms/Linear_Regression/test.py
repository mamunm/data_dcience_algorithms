#!/usr/bin/env python
# -*-coding: utf-8 -*-

import unittest
from lin_reg import LinearRegression
import numpy as np

class LinRegTest(unittest.TestCase):
    def test_predict(self):
        X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
        y = np.dot(X, np.array([1, 2])) + 3
        lr = LinearRegression()
        lr.fit(X, y)
        self.assertEqual(lr.predict(np.array([[3, 5], 
                                              [4, 5], 
                                              [2, 4]])).tolist(), 
                np.array([16., 17., 13.]).tolist())

if __name__ == '__main__':
    unittest.main()

