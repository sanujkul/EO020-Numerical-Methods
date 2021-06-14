#!/usr/bin/env python3.9

from sympy import *

#AVOID FOLLOWING LIBRARY AS IT WILL CAUSE ERROR IN FUNC (which has sine and cos)
#from math import *

#The variable x, for defining the function
x = Symbol('x')
#function in x
func = cos(x) - x*exp(x)
min_root_range = 0
max_root_range = 100



def numerical_bisection(fx):
    print('finding starting points between {} and {}'.format(min_root_range, max_root_range))
    a = findStartingPoints(fx);
    b = a+1;
    m = 0; #just initailizing

    fa = fx(a);
    fb = fx(b);

    print('Starting points are: a = {}, and b = {}\n'.format(a,b))
    print('STARTING BISECTION NOW!.......')
    
    i = 1;
    while True:
        m = (a+b)/2;
        fm = fx(m);

        print("===========================")
        print("\n{:02d}".format(i), end=". ")
        print("a={0:.6f}".format(a), end=" ");
        print("f(a)={0:.6f}".format(fa), end="\t");
        
        print("b={0:.6f}".format(b), end=" ");
        print("f(b)={0:.6f}".format(fb), end="\t");

        print("m={0:.6f}".format(m), end=" ");
        print("f(m)={0:.6f}".format(fm));
        
        i = i+1;
        
        if(abs(fm) < 0.000001):#Least count. Or this precision is enough
            break;

        if(fm*fa < 0):
            b = m;
            fb = fm;
        elif(fm*fb < 0):
            a = m;
            fa = fm;

    return m

# This function finds 2 starting: a,b points withing range
# such that f(a).f(b) = -ve
def findStartingPoints(fx):
    fa = fx(min_root_range);
    print('at x = {}, fx = {}'.format(min_root_range, fa))
    
    for i in range(min_root_range+1, max_root_range+1):
        fb = fx(i);
        #print('at x = {}, fx = {}'.format(i, fb))
        if(fa*fb < 0):
            return i-1
        fa = fb;



def main():
    global func;
    
    fx = lambdify(x, func)  
    print('Your function is: {}'.format(func));

    ans = numerical_bisection(fx)

    print('FOUND ROOT!')
    print('At x = {}, fx = {} ~ 0'.format(ans, fx(ans)))


if __name__ == "__main__":
    main()
