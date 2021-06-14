#!/usr/bin/env python3.9

from sympy import *

#The variable x, for defining the function
x = Symbol('x')
y = Symbol('y')
#function in x,y that is dy/dx (2nd order fun can be: 5*x**2 + 2*x + 1)
funcXY = x - y
# Given Initial condition (xo, yo)  
xo = 1
yo = 1
#and value of xn whose yn is to be found
xn = 1.1
#No of intervals to divide:
h = 0.01


#======================================================================
#======================================================================

#MAIN RUNGE KUTTA FUNCTION
# y1 = y1 = yo + (1/2)(k1 + k2)
# For this first find k1, k2
def rungeFunc(xo, yo, h, fxy):
    
    k1 = h*fxy(xo,yo)
    k2 = h*fxy(xo+h, yo+k1)

    print("k1 = {}, \t k2 = {}".format(k1,k2))
    
    y1 = yo + (1/2)*(k1 + k2)
    return y1
     


#======================================================================
#======================================================================

def rungeIteration(xo, yo, xn, h, fxy):

    print("------------------------------------")
    print("Printing k1, k2 and xold, yold, ynew for each iteration....")
    x_cur = xo
    y_cur = yo

    while(x_cur < xn):
        print("\n------------------------------------")
        y_new = rungeFunc(x_cur, y_cur, h, fxy)
        x_new = x_cur + h;
        print("x={0:.4f}".format(x_cur), end=" | ");
        print("y={0:.4f}".format(y_cur), end=" | ");
        print("y_new={0:.4f}".format(y_new));
        
        x_cur = x_new;
        y_cur = y_new;

    print("x={0:.4f}".format(x_cur), end=" | ");
    print("y={0:.4f}".format(y_cur));
    print("------------------------------------")
    
    return y_cur;
    

def main():
    global xo, yo, xn, h, funcXY;
    
    fxy = lambdify((x,y), funcXY)
    print('f(x,y) = dy/dx is: {} with (xo,yo): ({},{}) and xn = {} and h = {}'.format(funcXY,xo,yo,xn,h));
    
    valToFind = rungeIteration(xo, yo, xn, h, fxy);
    
    print("By Runge Kutta's method, at x = {}, y will be {}".format(xn,valToFind))

#======================================================================
#======================================================================

if __name__ == "__main__":
    main()
