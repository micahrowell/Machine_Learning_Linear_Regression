from computeCostMulti import *
"""
Perform a single gradient step on the parameter vector theta.
"""
def gradientDescentMulti(x,y,theta,alpha,num_iters):
    m = len(y)
    J_history = []

    for j in range(num_iters):

        sum = [0] * len(theta)

        for k in range(len(theta)):
            for i in range(m):
                if k == 0:
                    sum[k] += hypMulti(x,theta) - y[i]
                else:
                    sum[k] += (hypMulti(x,theta) - y[i]) * x[k-1][i]

        for i in range(len(theta)):
            sum[i] /= m

        for i in range(len(theta)):
            theta[i] -= alpha * sum[i]


        """
        sum0 = 0
        sum1 = 0
        
        for i in range(m):
            sum0 += hyp(x[i], theta) - y[i]
            sum1 += (hyp(x[i], theta) - y[i]) * x[i]

        sum0 /= m
        sum1 /= m

        theta[0] = theta[0] - alpha * sum0
        theta[1] = theta[1] - alpha * sum1
        """

        J_history.append(computeCostMulti(x, y, theta))


    return theta,J_history
