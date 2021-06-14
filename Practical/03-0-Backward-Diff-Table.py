#!/usr/bin/env python3.9

from sympy import *
from math import *

#Initialization part

#User will input givenX and givenXY
#givenX = [0.5, 0.7, 0.9, 1.1, 1.3, 1.5]
givenX = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5]
givenXY= {givenX[0]:7.989,
          givenX[1]:8.403,
          givenX[2]:8.781,
          givenX[3]:9.129,
          givenX[4]:9.451,
          givenX[5]:9.750}

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
        print("x{}={}".format(i, round(givenX[i],3)), end=" |\t");
        for j in range(0,j_range):
            print("{0:.5f}".format(backTable[i][j]), end =" |\t")
        print("")

    return backTable



#=====================================================
#=====================================================

def main():
    global givenX, givenXY, a, h, x;
    backwardDiffTable = createBackwardDiffTable();


if __name__ == "__main__":
    main()
