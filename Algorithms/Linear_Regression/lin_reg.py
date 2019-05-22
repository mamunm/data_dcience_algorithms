#!/usr/bin/env python
# -*-coding: utf-8 -*-

import numpy as np

class LinearRegression:
    '''An object to perform linear regression on data.'''
    def __init__(self, intercept=True):
        self.intercept = intercept
    
    def fit(self, X, y):
        '''
        Fit the linear regression model using least square method.
        Beta = (X^T X)^-1 XT y
        '''
        if self.intercept:
            X = np.append(np.ones([len(X), 1]), X, axis=1)
        self.params = np.matmul(np.matmul(np.linalg.inv(
            np.matmul(X.T, X)), X.T), y)
    
    def predict(self, X):
        if self.intercept:
            X = np.append(np.ones([len(X), 1]), X, axis=1)
        return np.matmul(self.params, X.T)
        



            


