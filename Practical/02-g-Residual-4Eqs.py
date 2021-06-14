from sympy import *

#This code could have been better if I had used arrays for a,b,c, d, R
numEquations = 3;

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

R1 = d1 - a1*x - b1*y - c1*z - e1*w;
R2 = d2 - a2*x - b2*y - c2*z - e2*w; 
R3 = d3 - a3*x - b3*y - c3*z - e3*w;
R4 = d4 - a4*x - b4*y - c4*z - e4*w;

ansPrecision = 0.01
roundOff = 5;

def whichIsMaxResidual(curR1, curR2, curR3, curR4):
    maxR = max(abs(curR1), abs(curR2), abs(curR3), abs(curR4));
    
    if(abs(curR1) == maxR):
        print("\ncurR1 is max")
        return 1; 
    elif(abs(curR2) == maxR):
        print("\ncurR2 is max")
        return 2;    
    elif(abs(curR3) == maxR):
        print("\ncurR3 is max")
        return 3;
    elif(abs(curR4) == maxR):
        print("\ncurR4 is max")
        return 4;
    


def residualMethod(calcR1, calcR2, calcR3, calcR4):
    global ansPrecision;

    tX = 0.0; tY = 0.0; tZ = 0.0; tW = 0.0#Absollute val of x, y, z
    Sx = 0.0; Sy = 0.0; Sz = 0.0; Sw = 0.0#For changing in residual
    
    curR1 = round(calcR1(tX,tY,tZ,tW),roundOff);
    curR2 = round(calcR2(tX,tY,tZ,tW),roundOff);
    curR3 = round(calcR3(tX,tY,tZ,tW),roundOff);
    curR4 = round(calcR4(tX,tY,tZ,tW),roundOff);

    i = 0;
    print("{}. (Sx,Sy,Sz,Sw)=({},{},{},{}) \t (X,Y,Z,W)=({},{},{},{}) \t (R1,R2,R3,R4)=({},{},{},{})".format(i,Sx,Sy,Sz,Sw,tX,tY,tZ,tW,curR1, curR2,curR3,curR4))
    
    while(abs(curR1) > ansPrecision or  abs(curR2) > ansPrecision or abs(curR3) > ansPrecision or abs(curR4) > ansPrecision):
        Sx = 0.0; Sy = 0.0; Sz = 0.0; Sw = 0.0;
        #Find which of these is max residual;
        maxResidualIs = whichIsMaxResidual(curR1, curR2, curR3, curR4)

        if(maxResidualIs == 1):
            Sx = round(curR1/a1,roundOff);
            tX = tX + Sx;
        elif(maxResidualIs == 2):
            Sy = round(curR2/b2,roundOff);
            tY = tY + Sy;
        elif(maxResidualIs == 3):
            Sz = round(curR3/c3,roundOff);
            tZ = tZ + Sz;
        elif(maxResidualIs == 4):
            Sw = round(curR4/e4,roundOff);
            tW = tW + Sw;

        curR1 = round(calcR1(tX,tY,tZ,tW),roundOff);
        curR2 = round(calcR2(tX,tY,tZ,tW),roundOff);
        curR3 = round(calcR3(tX,tY,tZ,tW),roundOff);
        curR4 = round(calcR4(tX,tY,tZ,tW),roundOff);
        i = i+1;
        print("{}. (Sx,Sy,Sz,Sw)=({},{},{},{}) \t (X,Y,Z,W)=({},{},{},{}) \t (R1,R2,R3,R4)=({},{},{},{})".format(i,Sx,Sy,Sz,Sw,tX,tY,tZ,tW,curR1, curR2,curR3,curR4))

#======================================================================
#======================================================================

def main():
    global R1, R2, R3;

    print('R1 = {} \nR2 = {} \nR3 = {} \nR3 = {}\n'.format(R1, R2, R3, R4));
    
    calcR1 = lambdify((x,y,z,w), R1)
    calcR2 = lambdify((x,y,z,w), R2)
    calcR3 = lambdify((x,y,z,w), R3)
    calcR4 = lambdify((x,y,z,w), R4)
    
    residualMethod(calcR1, calcR2, calcR3, calcR4);

    
#======================================================================
#======================================================================

if __name__ == "__main__":
    main()
