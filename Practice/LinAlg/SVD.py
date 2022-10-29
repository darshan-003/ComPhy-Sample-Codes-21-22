import numpy as np
from numpy.linalg import eig

AB = np.array([[2, 3, 4, 3], [3, -4, 2, -13], [1, 5, -3, 22]])


sigma1,V=eig((AB.T).dot(AB))
sigma2,U=eig(AB.dot(AB.T))

sigma=(U.T).dot(AB).dot(V)
# sigma=(U.T).dot(AB).dot(V)
print(U.dot(sigma).dot(V.T))


