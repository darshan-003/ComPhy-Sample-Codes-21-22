import numpy as np

def null(A, eps=1e-15):
    u, s, vh = np.linalg.svd(A)
    null_space = np.compress(s <= eps, vh, axis=0)
    return null_space.T



A = np.array([[2, 3, 4], [3, -4, 2], [1, 5, -3]])

eigval,eigvect = np.linalg.eig(A)


for i in  range(0,eigval.shape[0]):
    eigvector = np.zeros([A.shape[0], A.shape[0]])
    B=A
    for j in range(0,A.shape[0]):
        B[j][j]=B[j][j]-eigval[i]

    
print(null(A).T)


