import numpy as np
def norm(A):
    n=A.shape[0]
    m=A.shape[1]
    norm_=0
    for i in range(n):
        for j in range(m):
            norm_+=A[i][j]*A[i][j]

    return np.sqrt(norm_)


AB = np.array([[67, 5, 6, 7], [5, 4, 7, 8], [5, 6, 6, 3]])
n = AB.shape[0]
A = AB[:, :n]
norm_=norm(A)

Ainv=np.linalg.inv(A)

print(norm(A)*norm(Ainv))



