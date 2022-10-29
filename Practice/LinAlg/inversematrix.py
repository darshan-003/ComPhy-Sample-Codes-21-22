import numpy as np

def sub_from_row(A, diag_no, n):
    for i in range(0, n):
        if i <= diag_no:
            continue
        if A[i, diag_no] == 0:
            continue
        else:

            k = A[i, diag_no]
            A[i, :] = (A[i, :]) / k
            A[i, :] = A[diag_no, :]-A[i, :]

    return A


def upper_row_sub(A):
    n = A.shape[0]
    for i in range(0, n):
        for j in range(0, i):
            if A[j][i] != 0:

                k = A[j][i]
                A[j, :] = A[j, :]/k
                A[j, :] = A[j, :]-A[i, :]
        
                m = A[j][j]
                A[j, :] = A[j, :]/m
                

    return A


def inv(A1):
    I1 = np.array([[1], [0], [0]])
    I2 = np.array([[0], [1], [0]])
    I3 = np.array([[0], [0], [1]])

    A1 = np.hstack([A1, I1])
    A1 = np.hstack([A1, I2])
    A1 = np.hstack([A1, I3])
    A=A1
  
    for i in range(0, A.shape[0]):

        k = A[i][i]
       
        A[i, :] = A[i, :]/k
        A = sub_from_row(A, i, 3)

    A = upper_row_sub(A)
    return A[:,3:]


A = np.array([[2.0, 3.56, 4], [3, -4, 2], [1, 5, -3]])

print((inv(A)).dot(A))


