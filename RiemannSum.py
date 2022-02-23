#Prompts the user to create a normal distribution and then calculates the 
#riemann sum approximation of an integral with a specified range and accuracy 
def riemann():
    x1 = float(input('x1 = '))
    x2 = float (input('x2 = '))
    a = float(input('average = '))
    b = float (input('standard deviation = '))
    c = float (input('height = '))
    
    delta_x = ((x2-x1)/float(input('number of rectangles = ')))
    j = abs ((x2-x1)/delta_x)
    i = j
    n = 0
    A = 0.0
    x = x1

    while n < i:
        delta_A = c*(math.e**((-((x-a)**2))/b) * delta_x)
        x = x + delta_x
        A = A + delta_A
        n = n+1
    print('the area under the Curve from ' + str(x1) + ' to ' + str(x2) + ' is aproximately', A)

    x = np.arange(a-c, a+c, 0.01)
    y1 = c*math.e**((-((x-a)**2))/b)

    fig, (ax1) = plt.subplots(1, 1, sharex=True)

    ax1.plot(x, y1, color='black')
    ax1.fill_between(x, 0, y1, where = np.logical_and(x >= x1 , x <= x2))
    plt.show()
riemann()
