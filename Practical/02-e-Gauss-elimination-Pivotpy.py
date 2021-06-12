from fractions import Fraction
import fractions

#Specify number of equations.
#This code is for 3 or 4 equations
numEquations = 4;

#Pivot 1-> YES, 0 -> NO
pivot = True; 
#Init equations as with fractions with denominator 1
#Row 1
a11 = Fraction(2, 1);
a12 = Fraction(1, 1);
a13 = Fraction(1, 1);
a14 = Fraction(-2, 1);

#Row 2
a21 = Fraction(4, 1);
a22 = Fraction(0, 1);
a23 = Fraction(2, 1);
a24 = Fraction(1, 1);

#Row 3
a31 = Fraction(3, 1);
a32 = Fraction(2, 1);
a33 = Fraction(2, 1);
a34 = Fraction(0, 1);

#Row 4
a41 = Fraction(1, 1);
a42 = Fraction(3, 1);
a43 = Fraction(2, 1);
a44 = Fraction(-1, 1);

#Column Bmatrix
b1 = Fraction(-10, 1);
b2 = Fraction(8, 1);
b3 = Fraction(7, 1);
b4 = Fraction(-5, 1);


#NOTE: Python Matrix indexing starts from 0
if numEquations == 4:
    A = [[a11, a12, a13, a14],
         [a21, a22, a23, a24],
         [a31, a32, a33, a34],
         [a41, a42, a43, a44]]
    B = [b1, b2, b3, b4];
else:
    A = [[a11, a12, a13],
         [a21, a22, a23],
         [a31, a32, a33]]
    B = [b1, b2, b3];



#===========================================================
#===========================================================
def printAB_AuxMatrix():
    global A,B;
    n = len(A);

    for i in range(0,n):
        for j in range(0,n):
            print("{}".format(A[i][j]), end=" \t")
        print("{}".format(B[i]));




#===========================================================
#===========================================================
# row1, row2 are assumed to start with index 1
def swapRows(row1, row2):
    global A,B;
    n = len(A);

    #converting to with index 0:
    row1 = row1-1;
    row2 = row2-1;
    
    for i in range(0,n):
        tempA = A[row1][i];
        A[row1][i] = A[row2][i];
        A[row2][i] = tempA;

    tempB = B[row1];
    B[row1] = B[row2];
    B[row2] = tempB;

    

#===========================================================
#===========================================================
        # curRow is assumed to start with index ref 1.
        # A,B are assumptio with index starting with 1
        # all -1 are compensating for this difference
def pivotRows(currRow):
    global A,B;
    n = len(A);

    maxInColumn = A[currRow-1][currRow-1];
    maxRow = currRow-1;

    currColumn = currRow - 1; 
    
    for i in range(currRow, n):
        if (abs(A[i][currColumn]) > abs(maxInColumn)):
            maxInColumn = A[i][currColumn];
            maxRow = i;

    if(maxRow != currRow-1):
        #swap two rows
        swapRows(currRow, maxRow+1);


#===========================================================
#===========================================================    
def gauss_elimination():
    global A,B;
    n = len(A);

    
    #Current Row we are operating on
    currRow = 1;

    for currRow in range(1,n):
        print("We are at CurrRow = {}".format(currRow));
        
        if pivot:
            pivotRows(currRow);
            print("After pivoting, matrix is:");
            printAB_AuxMatrix();

        
        #Do the row opearion for upper triangular matrix
        for toEditRow in range(currRow+1,n+1):
            multiplyingFactor = A[toEditRow-1][currRow-1]/A[currRow-1][currRow-1]
            #Now change full toEditrow:
            for columnNo in range(currRow, n+1):
                A[toEditRow-1][columnNo-1] =  A[toEditRow-1][columnNo-1] - (multiplyingFactor * A[currRow-1][columnNo-1])
            B[toEditRow-1] = B[toEditRow-1] - (multiplyingFactor * B[currRow-1])
        print("After making 0s, matrix is:");
        printAB_AuxMatrix();

        print("=====================================\n")


                
#===========================================================
#===========================================================   
def main():
    global A, B;

    print("At beginning or Aux matrix is:")
    printAB_AuxMatrix();
    
    gauss_elimination();
    
    
    
    
    

if __name__ == "__main__":
    main()
