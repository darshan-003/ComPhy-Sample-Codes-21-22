import numpy as np
import matplotlib.pyplot as plt

def divided_diff(x,y):
    n=len(y)
    coef=np.zeros([n,n])

    coef[:,0]=y
    for i in range(1,n):
        for j in range (0,n-i):
            coef[j][i]= (coef[j+1][i-1]-coef[j][i-1])/(x[i+j]-x[j])

    return coef


def newt_poly(x_data,x,coef):
    y_data=np.zeros([x_data.shape[0]])
   
    for i in range(0, y_data.shape[0]):
        ans=np.zeros([x.shape[0]])
        ans[0] = coef[0]
        for j in range(1,x.shape[0]):
            ans[j] =  ( ( coef[j]/coef[j-1] ) * (x_data[i]-x[j-1]) * ans[j-1] )
            
            
        sum=0
        for k in range(0,ans.shape[0]):
            sum=sum+ans[k]
        
        
        y_data[i]=sum
    
    return y_data


 


        




    


x = np.array([-5, -1, 0, 2])
y = np.array([-2, 6, 1, 3])

coef=divided_diff(x,y)[0,:]

x_new = np.arange(-5, 2, .1)
y_new = newt_poly(x_new,x,coef)

print(y_new)

plt.figure(figsize=(12, 8))
plt.plot(x, y, 'bo')
plt.plot(x_new, y_new)
plt.show()

# print(coef)



