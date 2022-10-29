import numpy as np
import matplotlib.pyplot as plt
n=2
A=np.array([[3,8,22],[2,7,24]])
x=np.zeros(n)
xtemp=np.ones(n)

b=300
a=A.copy()

for i in range(n):
    for j in range(n):
        a[i][j]=a[i][j]/a[i][i]



for i in range(n):
    a[i][i]=0

while(b):
    
    for i in range(n):
        sum = 0
        for j in range(n):
            sum+=a[i][j] * x[j]
    
       
        x[i]=(a[i][n]-sum)
    
    b=b-1
    

for i in range(n):
    print("x", i, "=", x[i], "\n")
