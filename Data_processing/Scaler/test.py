#!/usr/bin/env python
# -*-coding: utf-8 -*-

import unittest
from scaler import Scaler
import numpy as np

class ScalerTest(unittest.TestCase):
    def test_minmax(self):
        data = [[-1, 2], [-0.5, 6], [0, 10], [1, 18]]
        standard = Scaler(scheme='minmax')
        self.assertEqual(standard.fit_transform(data).tolist(), 
                np.array([[0., 0.], [0.25, 0.25], 
                    [0.5, 0.5], [1., 1.]]).tolist())
        self.assertEqual(standard.transform([[2, 2]]).tolist(), 
                np.array([[1.5, 0.]]).tolist())
    
    def test_standard(self):
        data = np.array([[0, 0], [0, 0], [1, 1], [1, 1]])
        standard = Scaler(scheme='standard')
        self.assertEqual(standard.fit_transform(data).tolist(), 
                np.array([[-1., -1.], [-1., -1.], 
                          [ 1.,  1.], [ 1.,  1.]]).tolist())
        self.assertEqual(standard.transform([[2, 2]]).tolist(), 
                np.array([[3., 3.]]).tolist())

if __name__ == '__main__':
    unittest.main()

