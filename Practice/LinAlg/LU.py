import numpy as np

AB=np.array([[2,3,4,3],[3,-4,2,-13],[1,5,-3,22]])
n=AB.shape[0]
A=AB[:,:n]
from scipy.linalg import lu
P,L,U=lu(A)

AB[:, :n] = np.linalg.inv(P).dot(AB[:, :n])
AB[:, n] = np.linalg.inv(P).dot(AB[:, n])

print(AB)


# print(L,"\n")
# print(U,"\n")
# print(L.dot(U))
# print(P,"\n")

D=np.zeros(n)

for i in range(0,n):
    sum_=0
    for j in range (n):
        sum_+=L[i][j]*D[j]
    D[i]=AB[i][n]-sum_

print(L.dot(D))

X=np.zeros(n)
for i in range(n-1,-1,-1):
    sum_ = 0
    for j in range(n):
        sum_ += U[i][j]*X[j]
    X[i] =( D[i]-sum_)/U[i][i]

print(X)


