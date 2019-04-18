#!/usr/bin/env python
# -*-coding: utf-8 -*-

import numpy as np
from scipy.linalg import cho_factor, cho_solve

class GPRegressor:
    '''An object to perform gaussian process regression on data.'''
    def __init__(self, kernel=None, optimize=False):
        self.kernel = kernel
        self.optimize = optimize
    
    def fit(self, X, y):
        '''
        Fit the gaussian process regression model.
        '''
        self.X_train = X.copy()
        self.y_train = y.copy()
        K = self.kernel(X)
        self.L = cho_factor(K, lower=True)[0]
        self.a = cho_solve((self.L, True), y)
        self.lml = -0.5 * np.dot(y, self.a) 
        self.lml -= np.log(np.diag(self.L)).sum()
        self.lml -= X.shape[0] * 0.5 * np.log(2 * np.pi)

    def predict(self, X):
        self.mu = np.dot(self.kernel(X, self.X_train), self.a)
        #self.sigma = self.kernel(X, X) - np.matmul(np.linalg.inv(
        #    self.kernel(self.X_train)), self.kernel(self.X_train, X))
        return self.mu #self.sigma

    def lml(self, X, y):
        pass
        

class Kernel:
    '''An object to compute the covariance matrix of a given data based on 
    the kernel speicification. It only supports radial basis function 
    kernel.'''
    def __init__(self, constant=1.0, l_scale=1.0):
        self.constant = constant
        self.l_scale = l_scale
    def __repr__(self):
        return '{} RBF({})'.format(self.constant, self.l_scale)
    def __call__(self, X, Y=None):
        if not isinstance(Y, np.ndarray):
            X2 = X.copy()
        else:
            X2 = Y.copy()
        N_cov = np.zeros([X.shape[0], X2.shape[0]])
        for i in range(N_cov.shape[0]):
            for j in range(N_cov.shape[1]):
                N_cov[i, j] = np.linalg.norm((X[i] - X2[j])/self.l_scale) ** 2
        N_cov = np.exp(-0.5 * N_cov)
        if not isinstance(Y, np.ndarray):
            np.fill_diagonal(N_cov, 1)

        return self.constant * N_cov


if __name__ == "__main__":
    from sklearn.datasets import load_boston
    from sklearn.model_selection import train_test_split
    from sklearn.gaussian_process import GaussianProcessRegressor
    from sklearn.gaussian_process.kernels import RBF
    data = load_boston()
    X = data.data
    y = data.target
    Xt, Xtt, yt, ytt = train_test_split(X, y, train_size=0.8, random_state=42)
    gpr = GPRegressor(Kernel(1.0, 1.0))
    gpr.fit(Xt, yt)
    gprsk = GaussianProcessRegressor(RBF(1.0, 'fixed'), alpha=0)
    print(gpr.predict(Xtt))
    print(gpr.predict(Xt))
    print(gpr.lml)
    gprsk.fit(Xt, yt)
    print(gprsk.predict(Xtt))
    print(gprsk.predict(Xt))
    print(gprsk.log_marginal_likelihood_value_)

            


