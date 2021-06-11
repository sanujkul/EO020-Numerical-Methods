#!/usr/bin/env python3.9

from sympy import *

#The variable x, for defining the function
x = Symbol('x')
y = Symbol('y')
#function in x,y that is dy/dx (2nd order fun can be: 5*x**2 + 2*x + 1)
##funcXY = x + 2*y
funcXY = x**3 + y
# Given Initial condition (xo, yo)  
##xo = 1
##yo = 1
xo = 0
yo = 1
#and value of xn whose yn is to be found
xn = 0.02
#No of intervals to divide:
n = 2

#======================================================================
#======================================================================
#uses xo, xn, and n
#returns h
def getH():
    global xo,xn,n;
    return (xn - xo)/n

#======================================================================
#======================================================================

#MAIN EULER FUNCTION
# y(n+1) = yn + hf(xn,yn)
def eulerFunc(xn, yn, h, fxy):
    fxy_n = fxy(xn, yn)
    return yn + (h * fxy_n)
     


#======================================================================
#======================================================================

def eulerIteration(xo, yo, xn, h, fxy):

    print("------------------------------------")
    print("x \t y \t ynew=yold+h(dy/dx)")
    print("------------------------------------")
    x_cur = xo
    y_cur = yo

    while(x_cur < xn):
        y_new = eulerFunc(x_cur, y_cur, h, fxy)
        print("{0:.4f}".format(x_cur), end=" | ");
        print("{0:.4f}".format(y_cur), end=" | ");
        print("{0:.4f}".format(y_new));
        
        x_cur = x_cur + h;
        y_cur = y_new

    print("{0:.4f}".format(x_cur), end=" | ");
    print("{0:.4f}".format(y_cur));
    print("------------------------------------")
    
    return y_cur;
    

def main():
    global xo, yo, xn, n, funcXY;
    
    fxy = lambdify((x,y), funcXY)
    print('f(x,y) = dy/dx is: {} with (xo,yo): ({},{}) and xn = {}'.format(funcXY,xo,yo,xn));

    h = getH();
    print("\nValue of h is {}".format(h))
    valToFind = eulerIteration(xo, yo, xn, h, fxy);
    
    print("By Euler's method, at x = {}, y will be {}".format(xn,valToFind))

#======================================================================
#======================================================================

if __name__ == "__main__":
    main()
