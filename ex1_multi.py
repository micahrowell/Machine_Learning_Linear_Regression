from featureNormalize import *
from gradientDescentMulti import *

print 'Loading data . . .'
dataFile = open("ex1data2.txt","r")
x = []  # this array will hold an array of the features in ex1data2.txt
y = []  # this array will hold all of the y-values in ex1data2.txt

# I want an array of features where each element is an array of the number of those features, so first I need to
# grab the first line and establish x[] as such. This makes it easier to compute mu and sigma.
firstLine = dataFile.readline()
firstLine = firstLine.strip('\n')
firstLine = firstLine.split(',')
for i in range(len(firstLine)):
    if i != len(firstLine) - 1:
        # this line is why I can't just run a for loop on the data file
        x.append([float(firstLine[i])])
    else:
        y.append(float(firstLine[i]))

# for each line in the file, separate the values by the comma, cast them as a float, then append them to their
# respective arrays
for line in dataFile:
    line = line.strip('\n')
    line = line.split(',')
    for j in range(len(line)):
        if j != len(line) - 1:
            x[j].append(float(line[j]))
        else:
            y.append(float(line[j]))

m = len(y)

print 'First 10 examples from the dataset:\n'
string = 'x = ['
for i in range(len(x)):
    if i == len(x) - 1:
        string += str(x[i][0:10]) + ']'
    else:
        string += str(x[i][0:10]) + ', '
print string
print 'y = ' + str(y[0:10])

print '\nProgram paused. Press enter to continue.'
wait = raw_input()

print '\nNormalizing Features . . .'

mu, sigma = featureNormalize(x)

print 'x normalized: ' + str(x)
print 'mu = ' + str(mu)
print 'sigma = ' + str(sigma)

# translating x so that it is now an array of rows of data instead of an array of features
x1 = []
for j in range(len(x[0])):
    x1.append([0] * len(x))
    for i in range(len(x)):
        x1[j][i] = x[i][j]

print '\nRunning gradient descent . . .'
alpha = 0.01
num_iters = 400

theta,J_history = gradientDescentMulti(x1,y,[0,0,0], alpha,num_iters)

# theta = 334302, 100387, 3673

print 'theta after gradient descent: ' + str(theta)

x_new = [1650,3]
x_new = [(1650-mu[0])/sigma[0],(3-mu[1])/sigma[1]]

price = 0

for i in range(len(theta)):
    if i == 0:
        price += theta[i]
    else:
        price += theta[i] * x_new[i-1]

print '\nPredicted price of a 1650 sq-ft, 3 br house (using gradient descent): $' + str(price)
# print '\nProgram paused. Press enter to continue.'
# wait = raw_input()
