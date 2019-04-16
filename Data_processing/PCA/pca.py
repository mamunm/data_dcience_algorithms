#!/usr/bin/env python
# -*-coding: utf-8 -*-

#TODO implement varimax

from sklearn.preprocessing import MinMaxScaler
import numpy as np
import matplotlib.pyplot as plt

class PCA:
    def __init__(self, n_comp=2, normalize=False):
        self.n_comp = n_comp
        self.normalize = normalize
    
    def fit(self, X):
        self.tot_comp = X.shape[1]
        if self.normalize:
            scaler = MinMaxScaler()
            X = scaler.fit_transform(X)
        cov_mat = np.cov(X.T)
        eig_vals, eig_vecs = np.linalg.eig(cov_mat)
        eig_vals = abs(eig_vals)
        eval_sum = np.sum(eig_vals)
        self.all_explained_variance = eig_vals/eval_sum
        self.cum_explained_variance = np.cumsum(eig_vals/eval_sum) 
        argsort = np.argsort(eig_vals)[::-1][:self.n_comp]
        eig_vals, eig_vecs = eig_vals[argsort], eig_vecs[argsort]
        self.eigen_data = np.append(eig_vals.reshape(
            eig_vals.shape[0], 1), eig_vecs, axis=1)
        self.explained_variance = eig_vals/eval_sum
        self.proj_vec = np.stack([i[1:] for i in self.eigen_data], axis=1)
    def transform(self, X):
        return X.dot(self.proj_vec)
    def plot_explained_variance(self, fname='explained_variance.png'):
        with plt.style.context('seaborn-whitegrid'):
             plt.figure(figsize=(6, 4))
             plt.bar(range(self.tot_comp), 
                     self.all_explained_variance, 
                     alpha=0.8, align='center', color='teal',
                     label='individual explained variance')
             plt.step(range(self.tot_comp), 
                    self.cum_explained_variance, 
                    color='teal',
                    where='mid', 
                    label='cumulative explained variance')
             plt.ylabel('Explained variance ratio')
             plt.xlabel('Principal components')
             plt.legend(loc='best')
             plt.tight_layout()
             plt.savefig(fname)
             plt.show()


        



