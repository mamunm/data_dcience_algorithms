# Prinicpal component analysis 

Prinicipal component analysis is a great way to reduce the dimensionality of the data. It can be thought of as a variance conserving method where the data is projected onto canonical dimension and of those canonical dimensions the ones that explains the variance almost perfectly are kept and unimportant canonical dimensions are discarded. In this code, we will perform the Eigendecomposition method. Below I outline the step by step process:

1. Find the covariance matrix of all the features
2. Compute the Eigenvalues and Eigenvectors of the covariance matrix
3. Keep the Eigenvectors desired and discard the rest
4. Project the data onto this new Eigenvector direction
