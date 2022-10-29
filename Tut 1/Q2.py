import numpy as np


def norm(A):
    B=A**2
    n =A.shape[0]
    sum=0
    for i in range(n):
        sum+=B[i]
    
    return(np.sqrt(sum))


A=np.array([[0,0.1,0.2,0.3,0.5,1],[1,0.9,0.8,0.4,0.1,0],[0.9,1,0.8,0.5,0.2,0.1],[0.8,0.8,1,0.7,0.4,0.2],[0.4,0.5,0.7,1,0.6,0.3],[0.1,0.2,0.4,0.6,1,0.5]])
B=np.array([0.5,1,0.9,0.8,0.7,0.6])



a=0
b=0
c=0
d=0
e=0
f=0

temp_norm=1<<31

X=np.array([a,b,c,d,e,f])

stop=(0.5*10**(2-5))/100



for i in range(1,10000):
    f = B[0]-A.dot(X)[0]+f
    X = np.array([a, b, c, d, e, f])
    if(abs(norm(X)-temp_norm))/(norm(X))<stop:
        break
    

    temp_norm=norm(X)
    a = B[1]-A.dot(X)[1]+a
    X = np.array([a, b, c, d, e, f])
    if(abs(norm(X)-temp_norm))/(norm(X)) < stop:
        break

    temp_norm = norm(X)
    b = B[2]-A.dot(X)[2]+b
    X = np.array([a, b, c, d, e, f])

    if(abs(norm(X)-temp_norm))/(norm(X)) < stop:
        break

    temp_norm = norm(X)
    c = B[3]-A.dot(X)[3]+c
    X = np.array([a, b, c, d, e, f])

    if(abs(norm(X)-temp_norm))/(norm(X)) < stop:
        break

    temp_norm = norm(X)
    d = B[4]-A.dot(X)[4]+d
    X = np.array([a, b, c, d, e, f])

    if(abs(norm(X)-temp_norm))/(norm(X)) < stop:
        break
    temp_norm = norm(X)

    e = B[5]-A.dot(X)[5]+e
    X = np.array([a, b, c, d, e, f])

    if(abs(norm(X)-temp_norm))/(norm(X)) < stop:
        break
    temp_norm = norm(X)
   
print(a, b, c, d, e, f)
print(i)




