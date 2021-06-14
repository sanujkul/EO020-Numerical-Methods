#!/usr/bin/env python3.9

from sympy import *

#AVOID FOLLOWING LIBRARY AS IT WILL CAUSE ERROR IN FUNC (which has sine and cos)
#from math import *

#The variable x, for defining the function
x = Symbol('x')
#functionas  in x = func
#func = x**3 - 5*x + 1

#func = exp(-1*x)
func = (1 - x**2)**(0.33333333)

startSearchVal = 0.5
error = 0.0001


#In this code we have assumed that A will be fixed, since fA = +ve
# and B will vary 
def iterationMethod(fx, f1x):
    global startSearchVal, error ;

    xn = startSearchVal;

    print("\nGood starting is when |f1x(x)| < 1")
    #Good starting is when |f1x(x)| < 1 => condition to converge
    conditionVal = f1x(xn)
    print("xn = {} and f1x(xn) = {}".format(xn, conditionVal))
    
    while abs(conditionVal) >= 1:
        xn = xn+1;
        conditionVal = f1x(xn)
        print("xn = {} and f1x(xn) = {}".format(xn, conditionVal))

    print("\nOur starting point will be: {}".format(xn))
    #Now a good starting for xn is found
    i = 0
    print("x{} = {}, f(x) = {}".format(i, xn, xn - fx(xn)))
    
    while abs(xn - fx(xn)) > error:
        xn = fx(xn);
        i = i+1;
        print("x{} = {}, f(x) = {}".format(i, xn, xn - fx(xn)))
    
    return xn;


def main():
    global func;

    print('Your function is: {}'.format(func));

    f_prime = func.diff(x)
    print('\n 1st differntiation of fx is : {}'.format(f_prime))


    fx = lambdify(x, func)
    f1x = lambdify(x, f_prime)
    
    ans = iterationMethod(fx, f1x)

    print('FOUND ROOT!')
    print('At x = {}, fx = {} ~ 0'.format(ans, fx(ans)))


if __name__ == "__main__":
    main()
