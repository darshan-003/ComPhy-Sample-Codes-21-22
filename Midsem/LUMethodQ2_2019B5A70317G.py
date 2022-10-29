import numpy as np
import scipy as sc
from scipy.linalg import lu

A=np.array([[9.0,6,12],[6,3,11],[12,11,26]])
B=np.array([17.4,23.6,30.8])


def DoLittle(A):
    U=np.zeros([A.shape[0],A.shape[0]])
    L=np.eye(A.shape[0])
    n= A.shape[0]

    for i in range(0,n):
        U[0][i]=A[0][i]
    
    for i in range(0,n):
        L[i][0]= A[i][0]/U[0][0]


    for i in range(0,n):
        for j in range(0,n):

            if(j>=i):
                sum=0
                for k in range(0,i):
                    sum+=L[i][k]*U[k][j]

                U[i][j]=A[i][j]-sum

            else:
                sum=0.0
                for k in range(0,j):
                    sum+=L[i][k]*U[k][j]

                L[i][j]=(A[i][j]-sum)/U[j][j]

    

    return L,U


def fwdsub(L,B):
    n=L.shape[0]
    D=np.zeros(n)
    for i in range(0,n):
        sum=0
        for j in range(0,i):
            sum+=L[i][j]*D[j]

        D[i]=B[i]-sum

    
    return D

def backsub(U,D):
    n=U.shape[0]
    x=np.zeros(n)
    
    x[n-1]=D[n-1]/U[n-1][n-1]

    i=n-2
    while i>=0:
        sum=0
        j=n-1
        while j>=i+1:
           sum+= U[i][j]* x[j]
           j=j-1

        
        x[i]=(D[i]-sum)/U[i][i]
        i=i-1

    return x

def solveLU(L,U,B):
    D=fwdsub(L,B)
    X=backsub(U,D)

    return X


L,U=DoLittle(A)


print(L)

print(U)

print(solveLU(L,U,B))

