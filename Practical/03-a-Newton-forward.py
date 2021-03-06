#!/usr/bin/env python3.9

from sympy import *
from math import *

#Initialization part

#User will input givenX and givenXY
givenX = [8,10,12,14,16,18]
givenXY= {givenX[0]:10,
          givenX[1]:19,
          givenX[2]:32.5,
          givenX[3]:54,
          givenX[4]:89.5,
          givenX[5]:154}

#Initailzing a (starting value) and h(interval of differencing)
a = givenX[0]
h = givenX[1] - givenX[0]
#Value for x for which we want to interpolate for
x = 9

#This function will create and print a forward difefrence table
# First row (0) will be values of y corresponding to x
# Second row (1) will be Ist difefrence
def createForwardDiffTable():
    global givenX, givenXY;

    #For n given values we can find upto (n-1)th forward difference.
    #Indexing starts with 0.
    n = len(givenX);
    #Creating n x n 2d array. (Initializing with zeroes)
    forTable = zeros = [ [0] * n for _ in range(n)]

    for i in range(0,n):
        forTable[i][0] = givenXY[givenX[i]]

    #Now updating evey row.
    #j will be index for row (horizontal). jth index ==> jth forward difference.
    i_range = n;
    for j in range(1,n):
        i_range = i_range - 1;
        for i in range(0,i_range):
            forTable[i][j] = forTable[i+1][j-1] - forTable[i][j-1]
    
    #printing the difference table
    print("=====================================================")
    print("THE FORWARD DIFFERENCE TABLE IS:")
    print("=====================================================")
    j_range = n+1;
    for i in range(0,n):
        j_range = j_range - 1;
        
        print("x{}={:02d}".format(i,round(givenX[i],3)), end=" |\t");
        for j in range(0,j_range):
            print("{0:.5f}".format(forTable[i][j]), end =" |\t")
        print("")

    return forTable



#=====================================================
#=====================================================
def theNewtonForwardFormula(u, forwardDiffTable):
    global givenX, a;
    sum = 0;
    n = len(givenX)

    #Since only n-1 forward differences can be found using n values: 0 --> n-1
    for i in range(0,n):
        sum = sum + (factNotation(u,i)*forward_Diff(a, i, forwardDiffTable)/factorial(i))

    return sum;        

    
#=====================================================
#=====================================================
#To calculate u(u-1)(u-2).....(u-(n-1))
def factNotation(u,n):
    pdt = 1;
    for i in range(0,n):
        pdt = pdt*(u-i)
        
    return pdt

    
#=====================================================
#=====================================================
#This func will calculate the forward difference 
def forward_Diff(xo, n, forwardDiffTable):
    global givenX;
    index =  givenX.index(xo);
    return forwardDiffTable[index][n]



def main():
    global givenX, givenXY, a, h, x;
    forwardDiffTable = createForwardDiffTable();

    u = (x-a)/h

    print("x = {}, a = {}, h = {}, u = {}".format(x,a,h,u))
    
    interpolation = theNewtonForwardFormula(u, forwardDiffTable)

    print("The interpolation value at x = {} is {}".format(x, interpolation))
    
    

if __name__ == "__main__":
    main()
