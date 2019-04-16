#!/usr/bin/env python
# -*-coding: utf-8 -*-

from sklearn.datasets import load_iris
from pca import PCA

data = load_iris()
X = data.data
y = data.target
del data

pca = PCA(n_comp=2, normalize=True)
pca.fit(X)
print(pca.explained_variance)
pca.plot_explained_variance(fname='explained_variance.png')


