from computeCost import *

def gradientDescent(x, y, theta, alpha, iters):
    m = len(y)
    J_history = []

    for j in range(iters):
        """
        == == == == == == == == == == == YOUR CODE HERE == == == == == == == == == == ==
        Instructions: Perform a single gradient step on the parameter vector theta.
        
        Hint: While debugging, it can be useful to print out the values of the cost
              function(computeCost) and gradient here.
        == == == == == == == == == == == == == == == == == == == == == == == == == == ==
        """

        sum0 = 0
        sum1 = 0

        for i in range(m):
            sum0 += hyp(x[i],theta) - y[i]
            sum1 += (hyp(x[i],theta) - y[i]) * x[i]

        sum0 /= m
        sum1 /= m

        theta[0] = theta[0] - alpha * sum0
        theta[1] = theta[1] - alpha * sum1

        J_history.append(computeCost(x, y, theta))

    return theta
