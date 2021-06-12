#!/usr/bin/env python3.9

from sympy import *

#AVOID FOLLOWING LIBRARY AS IT WILL CAUSE ERROR IN FUNC (which has sine and cos)
#from math import *

#The variable x, for defining the function
x = Symbol('x')
#function in x
func = cos(x) - x*exp(x)
xA = 0
xB = 1


#In this code we have assumed that A will be fixed, since fA = +ve
# and B will vary 
def regulaFalsi_A(fx):
    global xA,xB;
    
    xn = xB;
    fxn = fx(xn);

    i = 0;
    print("x{} = {} \t f(xn) = {}".format(i, xn, fxn));
    
    while abs(fxn) > 0.01:
        x_new = regula_Falsi_Formula_A_fixed(fx, xA, xn)
        i = i+1;
        xn = x_new;
        fxn = fx(xn);
        
        print("x{} = {} \t f(xn) = {}".format(i, xn,fxn));


    return xn;

def regula_Falsi_Formula_A_fixed(fx, xA, xn):
    fa = fx(xA);
    fxn = fx(xn);

    x_new = xn - ((fxn/(fxn - fa))*(xn - xA))
    
    return x_new;
 


def main():
    global func;
    
    fx = lambdify(x, func)  
    print('Your function is: {}'.format(func));

    ans = regulaFalsi_A(fx)

    print('FOUND ROOT!')
    print('At x = {}, fx = {} ~ 0'.format(ans, fx(ans)))


if __name__ == "__main__":
    main()
