


###################################################################### Q3
import numpy as np
from numpy import linalg

# I : Inertia matrix
# t : diagonal matrix representing the eigenvalues
# q1 : eigenvectors

r1 = np.array([0, 1, 1])
r2 = np.array([1, 0, 1])
r3 = np.array([1, 1, 0])
I = np.zeros((3,3))

I[0][0] = (r1[1]**2+r1[2]**2)+(r2[1]**2+r2[2]**2)+(r3[1]**2+r3[2]**2)
I[1][1] = (r1[0]**2+r1[2]**2)+(r2[0]**2+r2[2]**2)+(r3[0]**2+r3[2]**2)
I[2][2] = (r1[0]**2+r1[1]**2)+(r2[0]**2+r2[1]**2)+(r3[0]**2+r3[1]**2)
I[0][1] = -(r1[0]*r1[1] + r2[0]*r2[1] + r3[0]*r3[1])
I[0][2] = -(r1[0]*r1[2] + r2[0]*r2[2] + r3[0]*r3[2])
I[1][2] = -(r1[1]*r1[2] + r2[1]*r2[2] + r3[1]*r3[2])
I[2][0] = I[0][2]
I[1][0] = I[0][1]
I[2][1] = I[1][2]

print(I)
################################################################ part b


t = I
q1 = np.zeros((3,3))
eigenvectors,r0 = linalg.qr(I)

for _ in range(1000):
    q,r = linalg.qr(t)
    t  = np.dot(r,q)
    q1 = np.dot(eigenvectors,q)
    q = q1
    
print(t)
# print(q1)
################################################################ part c
o,M = np.linalg.eig(I)
import scipy
from scipy import linalg
P,L,U = scipy.linalg.lu(I)
print(np.dot(np.dot(np.dot(np.linalg.inv(M),L),U),M))




