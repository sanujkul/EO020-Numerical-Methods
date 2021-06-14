#!/usr/bin/env python3.9

from sympy import *
from math import *

#Initialization part
#The variable x, for defining the function
x = Symbol('x')

#User will input givenX and givenXY
#givenX = [0.5, 0.7, 0.9, 1.1, 1.3, 1.5]
givenX = [-1, -0, 3, 6, 7]
givenXY= {givenX[0]:3,
          givenX[1]:-6,
          givenX[2]:39,
          givenX[3]:822,
          givenX[4]:1611}

#Initailzing a (starting value) and h(interval of differencing)
a = givenX[0]
h = givenX[1] - givenX[0]
#Value for x for which we want to interpolate for


#This function will create and print a forward difefrence table
# First row (0) will be values of y corresponding to x
# Second row (1) will be Ist difefrence
def createDividedDiffTable():
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
            forTable[i][j] = (forTable[i+1][j-1] - forTable[i][j-1])/(givenX[i+j]-givenX[i])
    
    #printing the difference table
    print("=====================================================")
    print("THE Divided DIFFERENCE TABLE IS:")
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
def theNewtonDivFormula(DivDiffTable):
    global givenX, a;
    global x;
    
    sum = 0;
    n = len(givenX)

    print("Puttig data in Newton Div Formula:")
    print("f(x) = ", end=" ")
    #Since only n-1 forward differences can be found using n values: 0 --> n-1
    for i in range(0,n):
        currTerm = factNotation(i)*giveDiv_Diff(a, i, DivDiffTable)
        print(currTerm, end=" + ")
        sum = sum + currTerm;

    return sum;



#=====================================================
#=====================================================
#In Newton divided differece:
# f(x) = f(xo) + (x-xo)(x-x1)f(xo,x1,x2) = ...+
# n belongs to 0 to n(length of x)
#This will return:
# (x-xo)(x-x1)....(x-xn-1)
def factNotation(n):
    global x, givenX;
    pdt = 1;

    if n==0:
        return 1;
    
    for i in range(0,n):
        pdt = pdt*(x-givenX[i])
        
    return pdt



#=====================================================
#=====================================================
#This func will calculate the forward difference 
def giveDiv_Diff(xo, n, DivDiffTable):
    global givenX;
    index =  givenX.index(xo);
    return DivDiffTable[index][n]




def main():
    global givenX, givenXY, a, h, x;
    DivDiffTable = createDividedDiffTable();

    #print(giveDiv_Diff(-4, 0, DivDiffTable))

    finalFormula = simplify(theNewtonDivFormula(DivDiffTable));
    print("\n=====================\n")
    print(finalFormula)

if __name__ == "__main__":
    main()
