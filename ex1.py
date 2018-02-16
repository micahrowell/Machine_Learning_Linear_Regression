import matplotlib.pyplot as plt
from warmupExercise import *
from gradientDescent import *

print 'Running warmUpExercise() ...'
print '5x5 Identity Matrix:\n'
matrix = warmupExercise()
for arr in matrix:
    print arr

print '\nProgram paused. Press enter to continue.'
wait = raw_input()

print '\nPlotting data...'
data = open("ex1data1.txt","r")
x = []  # this array will hold all of the x-values in ex1data1.txt
y = []  # this array will hold all of the y-values in ex1data1.txt
# for each line in the file, separate the values by the comma, cast them as a float, then append them to their
# respective arrays
for line in data:
    line = line.strip('\n')
    line = line.split(',')
    x.append(float(line[0]))
    y.append(float(line[1]))

print '\nProgram paused. Exit plot to continue.'

# plotting the data gathered from the file
plt.plot(x,y,'r+')
plt.xlabel('Population of City in 10,000s')
plt.ylabel('Profit in $10,000s')
plt.show()

# setting up some required values
iters = 1500
alpha = 0.01
theta = [0,0]
print '\nTesting the cost function...'
J = computeCost(x,y,theta)
print 'With theta = [0 , 0]\nCost computed = ' + str(J)
print 'Expected cost value (approx) 32.07'

theta = [-1,2]
J = computeCost(x,y,theta)
print '\nWith theta = [-1 , 2]\nCost computed = ' + str(J)
print 'Expected cost value (approx): 54.24'

print '\nProgram paused. Press enter to continue.'
wait = raw_input()

print '\nRunning gradient descent...'
theta = gradientDescent(x,y,theta,alpha,iters)
print 'Theta found by gradient descent: ' + str(theta)
print 'Expected theta values (approx): [-3.6303, 1.1664]'

print '\nProgram paused. Exit plot to continue.'

# calculating values of y according to the theta found from using gradient descent so that we can plot our linear
# regression model
y1 = []
for i in range(len(x)):
    y1.append(hyp(x[i],theta))
# plotting the linear regression model
plt.plot(x,y,'r+',x,y1,'-')
plt.xlabel('Population of City in 10,000s')
plt.ylabel('Profit in $10,000s')
plt.show()

# predicting future values based on the theta found using gradient descent
print 'For population = 35,000, we predict a profit of $' + str(hyp(35000,theta))
print 'For population = 70,000, we predict a profit of $' + str(hyp(70000,theta))
