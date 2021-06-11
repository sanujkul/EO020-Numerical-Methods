#!/usr/bin/env python3.9

from sympy import *

#The variable x, for defining the function
x = Symbol('x')
#function in x
func = exp(x) - 3**x
min_root_range = 0.3
max_root_range = 0.5;


####################################################################
####################################################################

def numerical_netwon(fx, f1x, f2x):
    xo = findStartingPoint_numerical(fx, f2x)
    
    while (abs(fx(xo)) > 0.0000001):
        xo = xo - (fx(xo)/f1x(xo));

    return xo;


####################################################################
####################################################################


# A good startinf form newton-rapson is that
# f(x).f''(x) > 0
def findStartingPoint_numerical(fx, f2x):
    a = findStartingPoint_bisection(fx);
    b = a+0.2;
    
    m = (a+b)/2;

    if(fx(m)*f2x(m) > 0):
        print("Returning starting value: m = {}".format(m))
        return m;

    if(fx(a)*f2x(a) > 0):
        print("Returning starting value: a = {}".format(a))
        return a;

    if(fx(b)*f2x(b) > 0):
        print("Returning starting value: b = {}".format(b))
        return b;

    print("\n NO GOOD STARTING POINT FOUND! Try something else");

####################################################################
####################################################################

# This function finds 2 starting: a,b points withing range
# such that f(a).f(b) = -ve
def findStartingPoint_bisection(fx):
    fa = fx(min_root_range);
    print('at x = {}, fx = {}'.format(min_root_range, fa))
    
    for i in range(min_root_range+0.2, max_root_range, 0.2):
        fb = fx(i);
        #print('at x = {}, fx = {}'.format(i, fb))
        if(fa*fb < 0):
            return i-0.2
        fa = fb;


####################################################################
####################################################################
def main():
    global func;
    print('Your function is : {}'.format(func))
    
    f_prime = func.diff(x)
    print('\n 1st differntiation of fx is : {}'.format(f_prime))

    f_2_prime = f_prime.diff(x);
    print('\n 2nd differntiation of fx is : {}'.format(f_2_prime))
    
    fx = lambdify(x, func)
    f1x = lambdify(x, f_prime)
    f2x = lambdify(x, f_2_prime)

    root = numerical_netwon(fx, f1x, f2x)

    print('Root, x = {} and f(x) = {} ~ 0'.format(root, fx(root)))

if __name__ == "__main__":
    main()
