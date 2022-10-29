import numpy as np
import matplotlib.pyplot as plt

def cont(x_points,i,n):


    eqns1 = np.zeros([3*n])
    eqns2 = np.zeros([3*n])

    if i==0:
        eqns2[0]=x_points[0]**2
        eqns2[1] = x_points[0]**1
        eqns2[2] = x_points[0]**0
        return eqns2
    
    if i==n:
        eqns1[0+3*(n-1)] = x_points[n]**2
        eqns1[1+3*(n-1)] = x_points[n]**1
        eqns1[2+3*(n-1)] = x_points[n]**0

        return eqns1

    else:
        eqns1[0+3*(i-1)] = x_points[i]**2
        eqns1[1+3*(i-1)] = x_points[i]**1
        eqns1[2+3*(i-1)] = x_points[i]**0

        eqns2[0+3*(i)] = x_points[i]**2
        eqns2[1+3*(i)] = x_points[i]**1
        eqns2[2+3*(i)] = x_points[i]**0

        return eqns1,eqns2




    


def deriv_cont( x_points,  i, n):
    
    eqns = np.zeros([3*n])
    eqns[(i-1)*3] = x_points[i]*2
    eqns[i*3] = -eqns[(i-1)*3]

    eqns[(i-1)*3 + 1] = 1
    eqns[i*3 + 1] = -1

    return eqns






def create_eqn(n,x_data):
    A=np.zeros([3*n,3*n])
    j=0

    for i in range(0,n+1):
        if(i==0 or i==n):
            A[j]=cont(x_data,i,n)
            j=j+1
        
        else:
            A[j],A[j+1]=cont(x_data,i,n)
            j=j+2
        


    for i in range(1,n):
        A[j] = deriv_cont(x_data, i, n)
       
        j = j+1
  
    A[j][0]=1
    return A


def create_B(n,y_data):
    B=np.zeros([3*n])
    
    B[0]=y_data[0]

    j=1
    for i in range(1,n):
        B[j]=y_data[i]
        B[j+1]=y_data[i]
        j=j+2

    B[j]=y_data[n]

    B[3*n-1]=0

    return B




x = np.array([0,10,15,20,22.5,30])
y = np.array([0,227.04,362.78,517.35,602.97,901.67])


A = create_eqn(x.shape[0]-1, x)
B = create_B(x.shape[0]-1, y)


print(A)

X = np.linalg.solve(A, B)


print(np.linalg.solve(A, B))




x_data=np.array(np.arange(0,30,0.01))
y_data=np.zeros([x_data.shape[0]])



for i in range(0, x_data.shape[0]):
    j = 0
    while x_data[i]>x[j+1]:
        j=j+1
    


    y_data[i]=X[3*j]*(x_data[i]**2)+X[3*j + 1]*(x_data[i])+X[3*j + 2]



 
plt.figure(figsize=(12, 8))
plt.plot(x, y, 'bo')
plt.plot(x_data, y_data)
plt.show()















