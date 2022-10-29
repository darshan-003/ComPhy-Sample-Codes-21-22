import numpy as np
import scipy as sc
import matplotlib.pyplot as plt 

def f(x):
    return np.exp(-x)*np.sin(4*x)


def singleonebythreesimpson(a,b):

    x_mid=(a+b)/2

    return(b-a)*(f(a)+4*f(x_mid)+f(b))/6
    
def Multipleonebythree(a,b,n):
    area=0
    h=(b-a)/n
    for i in range(0,n):
        area+=singleonebythreesimpson(a+i*h,a+(i+1)*h)

    return area


a=0.1
b=0.98*np.pi
h=0.097*np.pi

n=(b-a)/h
n=int(n)




print(Multipleonebythree(a,b,n))