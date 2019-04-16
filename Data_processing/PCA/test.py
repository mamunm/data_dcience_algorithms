#!/usr/bin/env python
# -*-coding: utf-8 -*-

import unittest
from pca import PCA
import numpy as np
from sklearn.datasets import load_boston

class PCATest(unittest.TestCase):
    def test_pca(self):
        X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
        pca = PCA(n_comp=2)
        pca.fit(X)
        self.assertEqual(np.allclose(pca.explained_variance,
            np.array([0.9924, 0.0075]), atol=1e-3), True)
    

if __name__ == '__main__':
    unittest.main()

