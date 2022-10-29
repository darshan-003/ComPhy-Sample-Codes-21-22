import numpy as np
import matplotlib.pyplot as plt



def Lag(i,n,x_given,x):
    ans=1
    for k in range(0,n):
        if k!=i:
            ans=ans*(x-x_given[k])/(x_given[i]-x_given[k])

    return ans


def poly(n,x_given,y_given,x_data):

    ans=np.zeros([x_data.shape[0]])


    for i in range(0,x_data.shape[0]):
        sum=0
        for j in range(0,n):
            sum=sum+(Lag(j,n,x_given,x_data[i])*y_given[j])
        ans[i]=sum


    return ans





x = np.array([-5, -3.11, 0, 2])
y = np.array([-2, 6, 1, 3])


x_new = np.arange(-5, 2.1, .1)
y_new = poly(x.shape[0],x,y,x_new)

print(y_new)

plt.figure(figsize=(12, 8))
plt.plot(x, y, 'bo')
plt.plot(x_new, y_new)
plt.show()
