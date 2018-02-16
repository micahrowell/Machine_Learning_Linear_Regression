def computeCost(x,y,theta):
    m = len(y)
    sum = 0
    for i in range(m):
        cost = hyp(x[i],theta) - y[i]
        cost *= cost
        sum += cost

    J = sum / (2*m)

    return J

# This is the linear regression hypothesis
def hyp(x,theta):
    return theta[0] + theta[1] * x