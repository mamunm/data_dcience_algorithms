#!/usr/bin/env python
# -*-coding: utf-8 -*-

import unittest
from gpr import Kernel
from gpr import GPRegressor
import numpy as np
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF

class LinRegTest(unittest.TestCase):
    def test_kernel(self):
        X = np.array([[6.320e-03, 1.800e+01], [2.731e-02, 0.000e+00]])
        K1 = Kernel(1.0, 1.0)
        K2 = Kernel(1.0, 2.0)
        K3 = Kernel(2.0, 2.0)
        np.testing.assert_allclose(K1(X), np.array([[1.00000000e+00, 4.40756028e-71],
       [4.40756028e-71, 1.00000000e+00]]))
        np.testing.assert_allclose(K2(X), np.array([[1.0000000e+00, 2.5766152e-18],
       [2.5766152e-18, 1.0000000e+00]]))
        np.testing.assert_allclose(K3(X), np.array([[2.00000000e+00, 5.15323041e-18],
       [5.15323041e-18, 2.00000000e+00]]))
    
    def test_predict(self):
        data = load_boston()
        X = data.data
        y = data.target
        Xt, Xtt, yt, ytt = train_test_split(X, y, 
                train_size=0.8, random_state=42)
        gpr = GPRegressor(Kernel(1.0, 1.0))
        gpr.fit(Xt, yt)
        mt, st = gpr.predict(Xt)
        mtt, stt = gpr.predict(Xtt)
        gprsk = GaussianProcessRegressor(RBF(1.0, 'fixed'), alpha=0)
        gprsk.fit(Xt, yt)
        mtsk, stsk = gprsk.predict(Xt, return_std=True)
        mttsk, sttsk = gprsk.predict(Xtt, return_std=True)
        np.testing.assert_allclose(mt, mtsk, atol=1e-3, rtol=1e-3)
        np.testing.assert_allclose(mtt, mttsk, atol=1e-3, rtol=1e-3)
        np.testing.assert_allclose(st, stsk, 
                atol=1e-3, rtol=1e-3, equal_nan=True)
        np.testing.assert_allclose(stt, sttsk, 
                atol=1e-3, rtol=1e-3, equal_nan=True)
        np.testing.assert_allclose(gpr.lml, 
                gprsk.log_marginal_likelihood_value_)

if __name__ == '__main__':
    unittest.main()

