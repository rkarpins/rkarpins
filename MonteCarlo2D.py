#Estimates the riemann sum of a function using the montecarlo approximation
import seaborn as sns
import sympy as sy
import numpy as np
import pandas as pd
import math
import random
import matplotlib.pyplot as plt
import re

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

fig, (ax1) = plt.subplots(1, 1, sharex=True)

def f(x):
    PDF = ((math.factorial(9)/(math.factorial(3)*math.factorial(5)))*(x**3)*(1-x)**5)
    return PDF

xmin = 0
xmax = 1


numSteps = 5000
ymin = f(xmin)
ymax = ymin

for i in range(numSteps):
    x = xmin + (xmax - xmin) * float(i) / numSteps
    y = f(x)
    if y < ymin: ymin = y
    if y > ymax: ymax = y

# Monte Carlo
rectArea = (xmax - xmin) * (ymax - ymin)
numPoints = 5000
hit = 0
x_point = []
y_point = []
miss_x = []
miss_y = []
test_value = 0.5
for j in range(numPoints):
    x = xmin + (xmax - xmin) *  np.random.random_sample()
    y = np.random.random_sample()
    if y < f(x) and x > test_value:
        x_point.append(x)
        y_point.append(y)
        hit += 1
    else:
        miss_x.append(x)
        miss_y.append(y)
fnArea = (float(hit) / numPoints)
print ("the probability that Y is greater than " + str(test_value) + " is aproximately " + str(fnArea))
ax1.set_ylim([-10,2.5])

ax1.plot(miss_x,miss_y,'bo')
ax1.plot(x_point,y_point,'ro')

a=[]
b=[]

for x in np.linspace(-0.3,1.5,1000):
    y= 504*((x**3)*(1-x)**5)
    a.append(x)
    b.append(y)

sns.lineplot(a,b, ax = ax1, legend = False, color = 'black').set(ylim=(0, 1), xlim = (0,1))

plt.show()
