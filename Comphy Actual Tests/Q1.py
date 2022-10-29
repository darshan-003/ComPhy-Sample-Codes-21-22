import numpy as np
import matplotlib.pyplot as plt


def H_matrix(λ):
    H = np.array([[1/2, 3*λ/4, 3*λ/(np.sqrt(2)), 0], [0, 3/2 + 15*λ/4, 0, 3 * np.sqrt(3/2)*λ],
                 [3*λ/(np.sqrt(2)), 0, 5/2 + 27*λ/4, 0], [0, 3 * np.sqrt(3/2)*λ, 0, 7/2 + 15*λ/4]])

    return H


def norms(A):
    n = A.shape[0]
    m = A.shape[1]
    norm_ = 0
    for i in range(n):
        for j in range(m):
            norm_ += A[i][j]*A[i][j]

    return np.sqrt(norm_)


H_inv = np.linalg.inv(H_matrix(0.4))

condition_no = norms(H_matrix(0.4)) * norms(H_inv)

print("Condition no. is ")
print(condition_no)

print("Which should be same as the one obtained by py library :" )
print(np.linalg.cond(H_matrix(0.4), 'fro'))


def norm(B):
    norm_ = 0
    for i in range(B.shape[0]):
        norm_ = norm_ + B[i]*B[i]
    return np.sqrt(norm_)


def QR(AB):
    Q = np.zeros([AB.shape[0], AB.shape[0]])

    Q[:, 0] = AB[:, 0]
    B = AB[:, 0]
    B = (1/norm(B)) * B
    Q[:, 0] = B

    n = 3
    for i in range(1, n+1):
        B = AB[:, i]
        temp = np.zeros(AB.shape[0])

        for j in range(0, i):  # Gram Schmidt Orthogonalization
            Proj = Q[:, j].dot(B)
            temp = temp + Proj * Q[:, j]

        B = B-temp
        B = B/norm(B)
        Q[:, i] = B

    Q = -Q

    R = np.linalg.inv(Q).dot(AB)

    return Q, R


H = H_matrix(0.4).copy()
for i in range(1, 1000):
    Q, R = QR(H)
    H = R.dot(Q)




print("Eigenvalues are :")

for i in range(0,4):
    print(H[i][i])


eigve,x=np.linalg.eig(H_matrix(0.4))

print("Eigenvector",eigve)
