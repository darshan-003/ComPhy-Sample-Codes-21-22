import numpy as np


def pivoted(B):
    A = B.copy()
    for i in range(0, A.shape[0]-1):

        max_ele = max(A[i:, i])
        if max_ele < -1*min(A[i:, i]):
            max_ele = -1*min(A[i:, i])

        for j in range(i, A.shape[0]):
            if(A[j, i] == max_ele):
                max_index = j
                break

        temp_ = A[i, :].copy()
        A[i, :] = A[max_index, :].copy()

        A[max_index, :] = temp_.copy()

    return A

def norm(A):
    B = A**2
    n = A.shape[0]
    sum = 0
    for i in range(n):
        sum += B[i]

    return(np.sqrt(sum))


A = np.array([[0, 0.1, 0.2, 0.3, 0.5, 1], [1, 0.9, 0.8, 0.4, 0.1, 0], [0.9, 1, 0.8, 0.5, 0.2, 0.1], [
             0.8, 0.8, 1, 0.7, 0.4, 0.2], [0.4, 0.5, 0.7, 1, 0.6, 0.3], [0.1, 0.2, 0.4, 0.6, 1, 0.5]])
# B = np.array([ 0.5, 1, 0.9, 0.8, 0.7, 0.6])

B = np.array([[0.5], [1], [0.9], [0.8], [0.7], [0.6]])

concat_mat=np.hstack([A,B])

new_concat_mat= pivoted(concat_mat)

A=new_concat_mat[:,:new_concat_mat.shape[0]]
B = new_concat_mat[:,new_concat_mat.shape[0]]



print(A,B)




# a = 1.88
# b = -0.36
# c = -1
# d = 0.44
# e = 0.40
# f = 0.39

a=1
b=1
c=1
d=1
e=1
f=1


temp_norm = 1 << 31

X = np.array([a, b, c, d, e, f])

stop = (0.5*10**(2-5))*100


for i in range(1, 10):

    a=(B[0]-A.dot(X)[0] + A[0][0]*a)/A[0][0]

    b = (B[1]-A.dot(X)[1] + A[1][1]*b)/A[1][1]

    c = (B[2]-A.dot(X)[2] + A[2][2]*c)/A[2][2]

    d = (B[3]-A.dot(X)[3] + + A[3][3]*d)/A[3][3]

    e = (B[4]-A.dot(X)[4] + A[4][4]*3*e)/A[4][4]

    f = (B[5]-A.dot(X)[5] + A[5][5]*f )/A[5][5]

    X = np.array([a, b, c, d, e, f])
    if(abs(norm(X)-temp_norm))/(norm(X)) < stop:
        break
    temp_norm = norm(X)

    print(a, b, c, d, e, f)

print(a, b, c, d, e, f)
print(i)


# f = B[0]-A.dot(X)[0]+f
#    X = np.array([a, b, c, d, e, f])
#    if(abs(norm(X)-temp_norm))/(norm(X)) < stop:
#         break

#     temp_norm = norm(X)
#     a = B[1]-A.dot(X)[1]+a
#     X = np.array([a, b, c, d, e, f])
#     if(abs(norm(X)-temp_norm))/(norm(X)) < stop:
#         break

#     temp_norm = norm(X)
#     b = B[2]-A.dot(X)[2]+b
#     X = np.array([a, b, c, d, e, f])

#     if(abs(norm(X)-temp_norm))/(norm(X)) < stop:
#         break

#     temp_norm = norm(X)
#     c = B[3]-A.dot(X)[3]+c
#     X = np.array([a, b, c, d, e, f])

#     if(abs(norm(X)-temp_norm))/(norm(X)) < stop:
#         break

#     temp_norm = norm(X)
#     d = B[4]-A.dot(X)[4]+d
#     X = np.array([a, b, c, d, e, f])

#     if(abs(norm(X)-temp_norm))/(norm(X)) < stop:
#         break
#     temp_norm = norm(X)

#     e = B[5]-A.dot(X)[5]+e
#     X = np.array([a, b, c, d, e, f])



