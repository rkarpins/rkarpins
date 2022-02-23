#Estimates the riemann sum of a 3 variable function using the montecarlo approximation
#Plots a 3D diagram of the integral using matplotlib
fig = plt.figure()
ax = fig.gca(projection='3d')

def f(X,Y):
    #Z = np.sin(np.sqrt(np.log(X+Y+1)))
    #Z = 1.5*((0.4**2-(0.6-((X-.5)**2+(Y-.5)**2)**0.5)**2)**0.5)+.2
    Z = 2*(np.sqrt(Y**Y) - np.sqrt(X**X) + .3)
    return Z

def param(X,Y):
    R = ((X-0.5)**2)+((Y-0.5)**2)
    return R
    
X = np.arange(0, 1.01, 0.25)
Y = np.arange(0, 1.01, 0.25)
X, Y = np.meshgrid(X, Y)
Z = f(X,Y)



ax.set_zlim(0, 1)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%25f'))


z = list(np.random.random_sample(2000))
x = list(np.random.random_sample(2000))
y = list(np.random.random_sample(2000))

hit_z = []
hit_x = []
hit_y = []
miss_z = []
miss_x = []
miss_y = []
hit = 0
miss = 0

for i in range(2000):
    if z[i] <= f(x[i],y[i]):# and  param(x[i],y[i])  <= .25:
    #if z[i] <= f(x[i],y[i]) and param(x[i],y[i]) <= z[i]:
        hit_z.append(z[i])
        hit_x.append(x[i])
        hit_y.append(y[i]) 
        hit += 1
    else:
        miss_z.append(z[i])
        miss_x.append(x[i])
        miss_y.append(y[i])
        miss += 1

ax.plot(hit_x,hit_y,hit_z, 'ro')
#ax.plot(miss_x,miss_y,miss_z, 'bo')

print((hit/(hit+miss)))
ax.plot_wireframe(X, Y, Z)
plt.show()
#the integral under the surface, and inside of the cylinder
#not displaying the misses due to the way matplotlib plots in 3D
