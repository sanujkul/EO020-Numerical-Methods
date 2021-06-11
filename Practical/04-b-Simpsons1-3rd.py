#!/usr/bin/env python3.9

from sympy import *


#The variable x, for defining the function
x = Symbol('x')
#function in x that is to be integrated (2nd order fun can be: 5*x**2 + 2*x + 1)
func = exp(sin(x))
# a -> starting limit
a = 0
# b -> end limit
b = 1.57079
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
        print(" -> {0:.4f}".format(yVals[i]))

    print("--------------------")
    
    return yVals;



#======================================================================
#======================================================================



#Main function that implements trapezoidal rule
#  = (h/3)[(y0 + yn) + 4(y1 + y3 + ....+ yn-1) + 2(y2 + y4 + .. + yn-2)]
def simpson1_3rdRule(y, h):
    n = len(y) - 1;

    #1. (y0 + yn)
    integration = y[0]+y[n];
    
    
    #2. sum of all the intermediate ornate: 1 to n-1
    for i in range(1,n):
        if(i%2 == 1): #if i is odd
            integration = integration + (4*y[i]);
        else:
            integration = integration + (2*y[i]);

    
    #3. multiply by h/3 
    integration = (h/3)*integration

    return integration;





#======================================================================
#======================================================================


def main():
    global a,b,n,func;
    
    fx = lambdify(x, func)  
    print('Function to integrate is: {} with limit: {} to {}'.format(func,a,b));

    h = getH();
    valueTable = getValueTable(fx,h);

    integration = simpson1_3rdRule(valueTable, h);

    print("The value of integration is {0:.7f}".format(integration));



#======================================================================
#======================================================================

if __name__ == "__main__":
    main()
