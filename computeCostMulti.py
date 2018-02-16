def computeCostMulti(x,y,theta):
    m = len(y)
    sum = 0
    for i in range(m):
        cost = hypMulti(x,theta) - y[i]
        cost *= cost
        sum += cost

    J = sum / (2*m)

    return J


def hypMulti(x, theta):
    hyp = 0
    # hyp_theta(x) = theta[0] + theta[1]x[1] + ... + theta[n]x[n]
    for j in range(len(x[0])):
        for i in range(len(theta)):
            if i == 0:
                hyp += theta[i]
            else:
                hyp += theta[i] * x[i-1][j]

    # return theta[0] + theta[1] * x
    return hyp
