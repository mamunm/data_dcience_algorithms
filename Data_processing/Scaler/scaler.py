#!/usr/bin/env python
# -*-coding: utf-8 -*-

import numpy as np

class Scaler:
    '''An object to perform scaling on data.
    Available methods are: minmax and standard.'''
    def __init__(self, scheme='minmax'):
        self.scheme = scheme
    
    def fit(self, X):
        '''Evaluate the fitting parameters.'''
        if not isinstance(X, np.ndarray):
            X = np.array(X)
        if self.scheme == 'minmax':
            self.min = X.min(axis=0)
            self.max = X.max(axis=0)
            self.range = self.max - self.min
        if self.scheme == 'standard':
            self.mean = X.mean(axis=0)
            self.std = X.std(axis=0)
    
    def transform(self, X):
        if not isinstance(X, np.ndarray):
            X = np.array(X)
        if self.scheme == 'minmax':
            return (X - self.min) / (self.max - self.min)
        if self.scheme == 'standard':
            return (X-self.mean)/self.std
    def fit_transform(self, X):
        self.fit(X)
        return self.transform(X)





            


