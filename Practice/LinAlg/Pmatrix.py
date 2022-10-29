import numpy as np

A = np.array([[2, 3, 4], [3, -4, 2], [1, 5, -3]])


def pivoted(B):
    A=B.copy()
    for i in range(0,A.shape[0]-1):

        max_ele=max(A[i:,i])
        if max_ele<-1*min(A[i:,i]):
            max_ele=-1*min(A[i:,i])
        
        
        for j in range(i,A.shape[0]):
            if(A[j,i]==max_ele):
                max_index=j
                break
        
        temp_=A[i,:].copy()
        A[i,:]=A[max_index,:].copy()

        A[max_index,:]=temp_.copy()

    return A
        

    







