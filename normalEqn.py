import numpy as np


def normalEqn(x, y):
    xMatrix = np.matrix(x)
    yMatrix = np.matrix(y)
    yMatrix = yMatrix.transpose() # turning 1 x N into N x 1
    xTranspose = xMatrix.transpose()
    inverse = np.linalg.inv(xTranspose * xMatrix)
    return inverse * xTranspose * yMatrix
