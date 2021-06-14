from sympy import *

#This code could have been better if I had used arrays for a,b,c, d, R
numEquations = 3;

#The variable x, for defining the function
x = Symbol('x')
y = Symbol('y')
z = Symbol('z')

#Equations in x, y, z: Give inputs here:
# ax + by + cz = d 
a1 = 9;     b1 = -2;    c1 = 1;     d1 = 50;
a2 = 1;     b2 = 5;     c2 = -3;    d2 = 18;
a3 = -2;     b3 = 2;    c3 = 7;    d3 = 19;


R1 = d1 - a1*x - b1*y - c1*z;
R2 = d2 - a2*x - b2*y - c2*z;
R3 = d3 - a3*x - b3*y - c3*z;

ansPrecision = 0.001
roundOff = 5;

def whichIsMaxResidual(curR1, curR2, curR3):
    if(abs(curR1) > abs(curR2)):
        if(abs(curR1) > abs(curR3)):
            return 1;
        else:
            return 3;
    else:
        if(abs(curR2) > abs(curR3)):
            return 2;
        else:
            return 3;
    


def residualMethod(calcR1, calcR2, calcR3):
    global ansPrecision;

    tX = 0.0; tY = 0.0; tZ = 0.0; #Absollute val of x, y, z
    Sx = 0.0; Sy = 0.0; Sz = 0.0; #For changing in residual
    
    curR1 = round(calcR1(tX,tY,tZ),roundOff);
    curR2 = round(calcR2(tX,tY,tZ),roundOff);
    curR3 = round(calcR3(tX,tY,tZ),roundOff);

    i = 0;
    print("{}. (Sx,Sy,Sz)=({},{},{}) \t (X,Y,Z)=({},{},{}) \t (R1,R2,R3)=({},{},{})".format(i,Sx,Sy,Sz,tX,tY,tZ,curR1, curR2,curR3))
    
    while(abs(curR1) > ansPrecision or  abs(curR2) > ansPrecision or abs(curR3) > ansPrecision):
        Sx = 0; Sy = 0; Sz = 0;
        #Find which of these is max residual;
        maxResidualIs = whichIsMaxResidual(curR1, curR2, curR3)

        if(maxResidualIs == 1):
            Sx = round(curR1/a1,roundOff);
            tX = tX + Sx;
        elif(maxResidualIs == 2):
            Sy = round(curR2/b2,roundOff);
            tY = tY + Sy;
        elif(maxResidualIs == 3):
            Sz = round(curR3/c3,roundOff);
            tZ = tZ + Sz;

        curR1 = round(calcR1(tX,tY,tZ),roundOff);
        curR2 = round(calcR2(tX,tY,tZ),roundOff);
        curR3 = round(calcR3(tX,tY,tZ),roundOff);
        i = i+1;
        print("\n{}. (Sx,Sy,Sz)=({},{},{}) \t (X,Y,Z)=({},{},{}) \t (R1,R2,R3)=({},{},{})".format(i,Sx,Sy,Sz,tX,tY,tZ,curR1, curR2,curR3))

#======================================================================
#======================================================================

def main():
    global R1, R2, R3;

    print('R1 = {} \nR2 = {} \nR3 = {} \n'.format(R1, R2, R3));
    
    calcR1 = lambdify((x,y,z), R1)
    calcR2 = lambdify((x,y,z), R2)
    calcR3 = lambdify((x,y,z), R3)
    
    residualMethod(calcR1, calcR2, calcR3);

    
#======================================================================
#======================================================================

if __name__ == "__main__":
    main()
