import numpy as np

def norm(B):
    norm_=0
    for i in range(B.shape[0]):
        norm_= norm_ + B[i]*B[i]
    return np.sqrt(norm_)


def QR(AB):
    Q=np.zeros([AB.shape[0],AB.shape[0]])

    Q[:, 0] = AB[:, 0]
    B=AB[:,0]
    B=(1/norm(B)) * B
    Q[:,0]=B


    n=3
    for i in range(1,n):
        B=AB[:,i]
        temp=np.zeros(AB.shape[0])

        for j in range(0,i):                    #Gram Schmidt Orthogonalization
            Proj=Q[:,j].dot(B)
            temp=temp+ Proj* Q[:,j]
        
        B=B-temp
        B=B/norm(B)
        Q[:,i]=B

    
    R=np.linalg.inv(Q).dot(AB)

    return Q, R





AB = np.array([[2, 3, 4], [3, -4, 2], [1, 5, -3]])

print(QR(AB))

# for i in range(0,100):
#     Q,R=QR(AB)
#     AB=R.dot(Q)





