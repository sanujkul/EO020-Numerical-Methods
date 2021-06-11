#!/usr/bin/env python3.9

from sympy import *
from math import *

#Initialization part

#User will input givenX and givenXY
givenX = [0.5, 0.7, 0.9, 1.1, 1.3, 1.5]
givenXY= {givenX[0]:0.47943,
          givenX[1]:0.64422,
          givenX[2]:0.78333,
          givenX[3]:0.89121,
          givenX[4]:0.96356,
          givenX[5]:0.99749}

#Initailzing a (starting value) and h(interval of differencing)
a = givenX[0]
h = givenX[1] - givenX[0]
#Value for x for which we want to interpolate for
x = 1.36


#This function will create and print a forward difefrence table
# First row (0) will be values of y corresponding to x
# Second row (1) will be Ist difefrence
def createBackwardDiffTable():
    global givenX, givenXY;

    #For n given values we can find upto (n-1)th forward difference.
    #Indexing starts with 0.
    n = len(givenX);
    #Creating n x n 2d array. (Initializing with zeroes)
    backTable = zeros = [ [0] * n for _ in range(n)]

    #Filling first column. Values of y for each x.
    for i in range(0,n):
        backTable[i][0] = givenXY[givenX[i]]

    #Now updating evey row.ffff
    #j will be index for row. jth index ==> jth forward difference.
    i_range = n+1;
    for j in range(1,n):
        i_range = i_range - 1;
        for i in range(n-1,n-i_range,-1):
            backTable[i][j] = backTable[i][j-1] - backTable[i-1][j-1]
    
    #printing the difference table
    print("=====================================================")
    print("THE BACKWARD DIFFERENCE TABLE IS:")
    print("=====================================================")
    j_range = 0;
    for i in range(0,n):
        j_range = j_range + 1;
        print("x{}={} \t ".format(i, givenX[i]), end=" ");
        for j in range(0,j_range):
            print("{0:.5f}".format(backTable[i][j]), end ="\t\t")
        print("")

    return backTable



#=====================================================
#=====================================================
def theNewtonBackwardFormula(u, backwardDiffTable):
    global givenX, a,h;
    sum = 0;
    n = len(givenX)

    lastX = givenX[n-1]
    #Since only n-1 backward differences can be found using n values: 0 --> n-1
    for i in range(0,n):
        sum = sum + (factAddNotation(u,i)*backward_Diff(lastX, i, backwardDiffTable)/factorial(i))

    return sum;        

    
#=====================================================
#=====================================================
#To calculate u(u+1)(u+2).....(u+(n-1))
def factAddNotation(u,n):
    pdt = 1;
    for i in range(0,n):
        pdt = pdt*(u+i)
        
    return pdt

    
#=====================================================
#=====================================================
#This func will calculate the forward difference 
def backward_Diff(xo, n, backwardDiffTable):
    global givenX;
    index =  givenX.index(xo);
    return backwardDiffTable[index][n]



def main():
    global givenX, givenXY, a, h, x;
    backwardDiffTable = createBackwardDiffTable();

    n = len(givenX)
    
    u = (x-givenX[n-1])/h

    print("x = {}, a = {}, h = {}, u = {}".format(x,a,h,u))
    
    interpolation = theNewtonBackwardFormula(u, backwardDiffTable)

    print("The interpolation value at x = {} is {}".format(x, interpolation))
    
    

if __name__ == "__main__":
    main()
