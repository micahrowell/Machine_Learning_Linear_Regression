from computeCostMulti import *

"""
Perform a single gradient step on the parameter vector theta.
"""


def gradientDescentMulti(x, y, theta, alpha, num_iters):
    m = len(y)
    j_history = []
    n = len(theta)
    for j in range(num_iters):
        sums = [0] * n

        for k in range(n):
            for i in range(m):
                if k == 0:
                    sums[k] += hypMulti(x[i], theta) - y[i]
                else:
                    sums[k] += (hypMulti(x[i], theta) - y[i]) * x[i][k - 1]
            sums[k] /= m
            sums[k] *= alpha
            sums[k] = theta[k] - sums[k]

        for p in range(n):
            theta[p] = sums[p]

        j_history.append(computeCostMulti(x, y, theta))

    return theta, j_history
