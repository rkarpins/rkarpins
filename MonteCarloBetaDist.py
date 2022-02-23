#Estimates Integral of a random Beta Distribution using Monte Carlo approximation

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

y = np.random.beta(4,6,size = 5000)

hit = 0
miss = 0 
neg_x = []
neg_y = []

pos_x = []
pos_y = []
x = list(1 - np.random.random_sample(5000))

for i in range(3000):
    #x = 1 - np.random.random_sample()
    if y[i] > 0.75:
        pos_x.append(x[i])
        pos_y.append(y[i])
        hit += 1
    else:
        neg_x.append(x[i])
        neg_y.append(y[i])
        miss += 1
plt.plot(pos_y,pos_x,'ro')
plt.plot(neg_y,neg_x,'bo')
plt.show()
print("The probability that Y is greater than .75 is approximately " + str(hit/(hit+miss)))
