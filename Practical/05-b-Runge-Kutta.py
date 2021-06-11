#!/usr/bin/env python3.9

from sympy import *

#The variable x, for defining the function
x = Symbol('x')
y = Symbol('y')
#function in x,y that is dy/dx (2nd order fun can be: 5*x**2 + 2*x + 1)
funcXY = x**2 + x
# Given Initial condition (xo, yo)  
xo = 0
yo = 1
#and value of xn whose yn is to be found
xn = 0.02
#No of intervals to divide:
h = 0.001


#======================================================================
#======================================================================

#MAIN RUNGE KUTTA FUNCTION
# y1 = y1 = yo + (k1 + 2k2 + 2k3 + k4)/6
# For this first find k1, k2, k3, k4
def rungeKuttaFunc(xo, yo, h, fxy):
    
    k1 = h*fxy(xo,yo)
    k2 = h*fxy(xo+(h/2), yo+(k1/2))
    k3 = h*fxy(xo+(h/2), yo+(k2/2))
    k4 = h*fxy(xo+h, yo+k3)

    print("k1 = {}, \t k2 = {}, \t k3 = {}, \t k4 = {}".format(k1,k2,k3,k4))
    
    y1 = yo + ((k1 + (2*k2) + (2*k3) + k4)/6)
    return y1
     


#======================================================================
#======================================================================

def rungeIteration(xo, yo, xn, h, fxy):

    print("------------------------------------")
    print("Printing k1, k2, k3, k4 and xold, yold, ynew for each iteration....")
    x_cur = xo
    y_cur = yo

    while(x_cur < xn):
        print("------------------------------------")
        y_new = rungeKuttaFunc(x_cur, y_cur, h, fxy)
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
