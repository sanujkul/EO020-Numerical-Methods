#!/usr/bin/env python3.9

from sympy import *

#The variable x, for defining the function
x = Symbol('x')
y = Symbol('y')
z = Symbol('z')

#Equations in x, y, z: Give inputs here:
# ax + by + cz = d 
#a1 = 28;     b1 = -4;    c1 = -1;     d1 = 32;
#a2 = 2;     b2 = 17;     c2 = 4;    d2 = 35;
#a3 = 1;     b3 = 3;    c3 = 10;    d3 = 24;

a1 = 8;     b1 = -3;    c1 = 2;     d1 = 20;
a2 = 4;     b2 = 11;     c2 = -1;    d2 = 33;
a3 = 6;     b3 = 3;    c3 = 12;    d3 = 36;

precision = 0.00001

def main():
    global x,y,z;
    global precision;
    global a1,b1,c1,d1,a2,b2,c2,d2,a3,b3,c3,d3;
    
    eq_x = (d1 - b1*y - c1*z)/a1;
    eq_y = (d2 - a2*x - c2*z)/b2;
    eq_z = (d3 - a3*x - b3*y)/c3;

    x_val = lambdify([y, z], eq_x)
    y_val = lambdify([x, z], eq_y)
    z_val = lambdify([x, y], eq_z)

    x0 = x_val(0,0)
    y0 = y_val(0,0)
    z0 = z_val(0,0)
    print("0. x = {} \t y = {} \t z = {}".format(x0,y0,z0))
    
    x1 = x_val(y0,z0)
    y1 = y_val(x1,z0)
    z1 = z_val(x1,y1)

    #print(x0,y0,z0)
    #print(x1,y1,z1)

    count = 1;
    print("{}. x = {} \t y = {} \t z = {}".format(count,x1,y1,z1))
    
    while (abs(x1-x0) > precision) or (abs(y1-y0) > precision) or (abs(z1-z0) > precision):
        x0 = x1
        y0 = y1
        z0 = z1

        x1 = x_val(y0,z0)
        y1 = y_val(x1,z0)
        z1 = z_val(x1,y1)

        count += 1;
        print("{}. x = {} \t y = {} \t z = {}".format(count,x1,y1,z1))

    print("Solution of given equation is : ({}, {}. {})".format(x1,y1,z1))
    print('Number of iterations = {}'.format(count))
        

if __name__ == "__main__":
    main()
