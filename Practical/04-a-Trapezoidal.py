#!/usr/bin/env python3.9

from sympy import *

#The variable x, for defining the function
x = Symbol('x')
#function in x that is to be integrated (2nd order fun can be: 5*x**2 + 2*x + 1)
func = sin(x)/x
# a -> starting limit (Since division by 0 is not allowed, making it very small)
a = 0.000000000001
# b -> end limit
b = 3.1415926
# n -> number of intervals
n = 10


#======================================================================
#======================================================================

#uses a, b, and n
#returns h
def getH():
    global a,b,n;
    return (b-a)/n


#======================================================================
#======================================================================


#This returns an array with values: y0, y1, y2, ...., yn
# corresponding to xo, x1, x2, ...., xn
def getValueTable(fx,h):
    global a,b,n;

    #Initilizing with 0
    #There are (n+1) x values for n intervals:xo, x1, x2, ...., xn
    xVals = [0] * (n+1)

    #Corresponding values (y) of fucntion for x 
    yVals = [0] * (n+1)


    print("--------------------")
    print("x \t-> y")
    print("--------------------")
    #print("Printing ordinates: ", xVals, yVals)
    for i in range(len(xVals)):
        xVals[i] = a + (i*h);
    
        yVals[i] = fx(xVals[i]);
        
        print("{0:.4f}".format(xVals[i]), end=" ")
        print(" -> {0:.8f}".format(yVals[i]))

    print("--------------------")
    
    return yVals;



#======================================================================
#======================================================================



#Main function that implements trapezoidal rule
#  = h[1/2(y0 + yn) + (y1 + y2 + ....+ yn-1)]
def trapezoidalRule(y, h):
    n = len(y) - 1;

    #1. mean of first and last ornate
    integration = (y[0]+y[n])/2;
    
    
    #2. sum of all the intermediate ornate: 1 to n-1
    for i in range(1,n):
        integration = integration + y[i];

    
    #3. multiply by h (distance b/w 2 consecutive ornate)
    integration = h*integration

    return integration;





#======================================================================
#======================================================================


def main():
    global a,b,n,func;
    
    fx = lambdify(x, func)  
    print('Function to integrate is: {} with limit: {} to {}'.format(func,a,b));

    h = getH();
    valueTable = getValueTable(fx,h);

    integration = trapezoidalRule(valueTable, h);

    print("The value of integration is {0:.8f}".format(integration));



#======================================================================
#======================================================================

if __name__ == "__main__":
    main()
