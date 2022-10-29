import numpy as np
from numpy import linalg
from numpy.linalg import eig


def norm(A):
    n = A.shape[0]
    m = A.shape[1]
    norm_ = 0
    for i in range(n):
        for j in range(m):
            norm_ += A[i][j]*A[i][j]

    return np.sqrt(norm_)


H = np.array([[0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0],
             [0.0, 0.0, 0.0, 0.0],  [0.0, 0.0, 0.0, 0.0]])

for i in range(0, 4):
    for j in range(0, 4):
        H[i][j] = (float)((2*(i+1) + (j+1) - 1))**(-1)


eigenvalue, eigenvector = eig(H)

H_inv = linalg.inv(H)


#  M= max( Norm(Ax)/Norm(A) ) = |A|
#
#  m = min( ( Norm(Ax) )/ Norm(A) ) =min ( |y| /(|A^-1 y|) ) =  max(1/ ( |A^-1 y |/|y| )) = 1/|A^-1|
#
#  C(A) =M/m = |A| * |A^-1|
#


condition_no = norm(H)*norm(H_inv)

determinant = linalg.det(H)


print("Eigenvalue = ", eigenvalue, "\n")
print("Eigenvector = ", eigenvector, "\n")
print("Condition No. = ", condition_no, "\n")
print("Determinant = ", determinant, "\n")
