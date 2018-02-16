import numpy as npy

"""
For each feature dimension, compute the mean of the feature and subtract it from the
dataset, storing the mean in mu. Next, compute the standard deviation of each feature
and divide each feature by its standard deviation, storing the standard deviation in sigma.
"""

def featureNormalize(x):
    mu = []
    sigma = []
    for i in range(len(x)):
        mu.append(npy.mean(x[i]))
        sigma.append(npy.std(x[i]))
        for j in range(len(x[i])):
            x[i][j] = ((x[i][j] - mu[i]) / sigma[i])

    return mu,sigma
