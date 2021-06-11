#!/usr/bin/env python3.9

from sympy import *
from math import *

x = Symbol('x')

f = 2*x**2+3
f_prime = f.diff(x)

f2 = f * f_prime;

print(f)

print(f_prime)

print(f2)



f = lambdify(x, f)
f_prime = lambdify(x, f_prime)

f3 = f_prime(x+2)
print(f3)

print(f3(2))

print(f_prime)


