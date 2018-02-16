def computeCostMulti(x,y,theta):
    m = len(y)
    sum = 0
    for i in range(m):
        cost = hypMulti(x[i],theta) - y[i]
        cost *= cost
        sum += cost

    J = sum / (2*m)

    return J


def hypMulti(x, theta):
    hyp = 0
    for i in range(len(theta)):
        if i == 0:
            hyp += theta[i]
        else:
            hyp += theta[i] * x[i-1]

    return hyp
