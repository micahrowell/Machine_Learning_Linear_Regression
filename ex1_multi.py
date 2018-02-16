from featureNormalize import *
from gradientDescentMulti import *

print 'Loading data . . .'
dataFile = open("ex1data2.txt","r")
x = []  # this array will hold an array of the features in ex1data2.txt
y = []  # this array will hold all of the y-values in ex1data2.txt

# I want an array of features where each element is an array of the number of those features, so first I need to
# grab the first line and establish x[] as such
firstLine = dataFile.readline()
firstLine = firstLine.strip('\n')
firstLine = firstLine.split(',')
for i in range(len(firstLine)):
    if i != len(firstLine) - 1:
        # this line is why I can't just run a for loop on the data file
        x.append([float(firstLine[i])])
    else:
        y.append(float(firstLine[i]))

#print x
#print y

# for each line in the file, separate the values by the comma, cast them as a float, then append them to their
# respective arrays
for line in dataFile:
    line = line.strip('\n')
    line = line.split(',')
    for j in range(len(line)):
        xEntry = []
        if j != len(line) - 1:
            x[j].append(float(line[j]))
        else:
            y.append(float(line[j]))
#print x
#print y

m = len(y)

print 'First 10 examples from the dataset:\n'
string = 'x = ['
for i in range(len(x)):
    if i == len(x) - 1:
        string = string + str(x[i][0:10]) + ']'
    else:
        string = string + str(x[i][0:10]) + ', '
print string
print 'y = ' + str(y[0:10])

print '\nProgram paused. Press enter to continue.'
wait = raw_input()

print '\nNormalizing Features . . .'

mu, sigma = featureNormalize(x)

print 'x normalized: ' + str(x)
print 'mu = ' + str(mu)
print 'sigma = ' + str(sigma)

print '\nRunning gradient descent . . .'
alpha = 0.01
num_iters = 400

theta,J_history = gradientDescentMulti(x,y,[0,0,0], alpha,num_iters)

# theta = 334302,100387, 3673

print 'theta after gradient descent: ' + str(theta)
print 'J_history: ' + str(J_history)
