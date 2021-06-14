#!/usr/bin/env python3.9

from sympy import *

#The variable x, for defining the function
x = Symbol('x')
y = Symbol('y')

#function in x,y that is dy/dx (2nd order fun can be: 5*x**2 + 2*x + 1)
#funcXY = (1+y)* x**2
funcXY = x**2 + y**2


# Given Initial condition (xo, yo)  
#X = [1,     1.1,    1.2,    1.3,    1.4]
#Y = [1,     1.233,  1.548,  1.979,  0]
X = [-0.1,      0,      0.1,        0.2,    0.3]
Y = [0.9087,    1,      1.1113,     1.2506,  0]

#and value of xn whose yn is to be found
#xn = 0.3
#No of intervals to divide:
h = 0.1

#======================================================================
#======================================================================

#Returns value of yn corresponding to xn
# Predictor formula is:
# yn+1, p = yn-3 + (4h/3)(2fn-2 - fn-1 + 2fn)
def milnesPredictor(fxy, Fxy):
    global X, Y, xn, h;

    #Assume n=3 in above function equation
    y4p = Y[0] + ((4*h)/3)*((2*Fxy[1]) - Fxy[2] + (2*Fxy[3]))

    return y4p;
        
#======================================================================
#======================================================================

#Returns value of yn corresponding to xn
# Corrector formula is:
# yn+1, c = yn-1 + (h/3)(fn-1 + 4*fn + fn+1)
# n=3, y4,c = y2 + (h/3)(f2 + 4f3 + f4)
def milnesCorrector(fxy, Fxy):
    global X, Y, xn, h;

    #Assume n=3 in above function equation
    y4c = Y[2] + (h/3)*((Fxy[2]) + (4*Fxy[3]) + Fxy[4])

    return y4c;


#======================================================================
#======================================================================

def main():
    global X, Y, xn, h, funcXY;
    
    fxy = lambdify((x,y), funcXY)
    print('f(x,y) = dy/dx is: {} and h = {}'.format(funcXY,h));

    #Array that have dy/dx vales corresponding to xo,yo & x1,y1 .... 
    Fxy = [0,0,0,0,0];

    for i in range(0,4):
        Fxy[i] = fxy(X[i], Y[i]);

    print("Applying Milne's Predictor Formula:")
    print("yn+1, p = yn-3 + (4h/3)(2fn-2 - fn-1 + 2fn)")
    print("For n=3, y4,p = y0 + (4h/3)(2f1 - f2 + 2f3)")
    Y[4] = milnesPredictor(fxy, Fxy);
    print("The value of y4p is {}".format(Y[4]))

    Fxy[4] = fxy(X[4], Y[4])

    print("\n==================== \n====================")
    print("Applying Milne's Corrector Formula:")
    print("yn+1, c = yn-1 + (h/3)(fn-1 + 4*fn + fn+1)")
    print("For n=3, y4,c = y2 + (h/3)(f2 + 4f3 + f4)")
    Y[4] = milnesCorrector(fxy, Fxy);
    print("The value of y4p is {}".format(Y[4]))
    
    
#======================================================================
#======================================================================

if __name__ == "__main__":
    main()
