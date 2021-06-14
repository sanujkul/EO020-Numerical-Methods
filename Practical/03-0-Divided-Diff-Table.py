#!/usr/bin/env python3.9

from sympy import *
from math import *

#Initialization part

#User will input givenX and givenXY
#givenX = [0.5, 0.7, 0.9, 1.1, 1.3, 1.5]
givenX = [-4, -1, 0, 2, 5]
givenXY= {givenX[0]:1245,
          givenX[1]:33,
          givenX[2]:5,
          givenX[3]:9,
          givenX[4]:1335}

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



def main():
    global givenX, givenXY, a, h, x;
    forwardDiffTable = createDividedDiffTable();


if __name__ == "__main__":
    main()
