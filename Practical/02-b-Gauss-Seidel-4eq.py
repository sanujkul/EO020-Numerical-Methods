#!/usr/bin/env python3.9

from sympy import *

#The variable x, for defining the function
x = Symbol('x')
y = Symbol('y')
z = Symbol('z')
w = Symbol('w')

#Equations in x, y, z: Give inputs here:
# ax + by + cz + ew = d 
a1 = 8;     b1 = 1;    c1 = 1;     e1 = 1;  d1 = 14;
a2 = 2;     b2 = 10;     c2 = 3;    e2 = 1;  d2 = -8;
a3 = 1;     b3 = -2;    c3 = -20;    e3 = 3;  d3 = 111;
a4 = 3;     b4 = 2;    c4 = 2;    e4 = 19;  d4 = 53;

precision = 0.00001

def main():
    print("This is Gauss-Seidel for 4 equations");
    global x,y,z;
    global precision;
    global a1,b1,c1,e1,d1;
    global a2,b2,c2,e2,d2;
    global a3,b3,c3,e3,d3;
    global a4,b4,c4,e4,d4;
    
    eq_x = (d1 - b1*y - c1*z - e1*w)/a1;
    eq_y = (d2 - a2*x - c2*z - e2*w)/b2;
    eq_z = (d3 - a3*x - b3*y - e3*w)/c3;
    eq_w = (d4 - a4*x - b4*y - c4*z)/e4;

    x_val = lambdify([y, z, w], eq_x)
    y_val = lambdify([x, z, w], eq_y)
    z_val = lambdify([x, y, w], eq_z)
    w_val = lambdify([x, y, z], eq_w)
    
    #Init by x0 = y0 = z0 = 0
    x0 = x_val(0,0,0)
    y0 = y_val(0,0,0)
    z0 = z_val(0,0,0)
    w0 = w_val(0,0,0)
    
    print("0. x = {} \t y = {} \t z = {} \t w = {}".format(x0,y0,z0,w0))
    
    x1 = x_val(y0,z0,w0)
    y1 = y_val(x1,z0,w0)
    z1 = z_val(x1,y1,w0)
    w1 = w_val(x1,y1,z1)
    
    count = 1;
    print("{}. x = {} \t y = {} \t z = {} \t w = {}".format(count,x1,y1,z1,w1))
    
    while (abs(x1-x0) > precision) or (abs(y1-y0) > precision) or (abs(z1-z0) > precision):
        x0 = x1
        y0 = y1
        z0 = z1
        w0 = w1

        x1 = x_val(y0,z0,w0)
        y1 = y_val(x1,z0,w0)
        z1 = z_val(x1,y1,w0)
        w1 = w_val(x1,y1,z1)

        count += 1;
        print("{}. x = {} \t y = {} \t z = {} \t w = {}".format(count,x1,y1,z1,w1))

    print("Solution of given equation is :\nx={},\ny={}. \nz={}, \nw={}".format(round(x1,5),round(y1,5),round(z1,5),round(w1,5)))
    print('Number of iterations = {}'.format(count))
        

if __name__ == "__main__":
    main()
