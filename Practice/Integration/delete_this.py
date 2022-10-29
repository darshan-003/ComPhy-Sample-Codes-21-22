import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 2000*np.log((140000)/(140000-2100*x)) - 9.8*x


def g(x,a,b): 
   return f(((b+a)+(b-a)*x)/2)


def gaussQuadratic(a,b):
    return ( g(-1/np.sqrt(3),a,b)+g(1/np.sqrt(3),a,b) ) * ((b-a)/2)

def ModifiedMonteCarlo(a,b,n):
    sum=0
    for i in range(0,n):
       xi=a+(b-a)*np.random.randint(0,1000000)/1000000
       sum+=f(xi)
        

   
    return (b-a)*sum/n


def MultipleTrap(a,b,n):
    h=(b-a)/n
    sumpoints=0
    for i in range(1,n):
        sumpoints+=f(a+i*h)

    return (h/2)*(f(a)+f(b)+2*sumpoints)
def roomberg(a,b,n,row):
    Mat=np.zeros([row,row])
    Mat+=0.0

    
    for i in range(0,row):
        Mat[i][0]=MultipleTrap(a,b,n)
        n=n*2

    
    
    for q in range(1,row):
        for p in range(0,row-q):
            Mat[p][q]= (pow(4,q)*Mat[p+1][q-1]-Mat[p][q-1])/( pow(4,q)-1)



    return Mat
    




def checkCorrectness(x):
    r=abs((x[0][1]-x[0][0])/(x[0][2]-x[0][1]))
    if r>3.5:
        return "Roomberg Converging Quickly, No Additional Change of Variables Reqd"
    else:
        return "Roomberg not converging quickly "




print(gaussQuadratic(8,30))
# F
print(ModifiedMonteCarlo(8,30,100000))
# F
Mat=roomberg(8,30,4,6)
# F
print(checkCorrectness(Mat))
# F
print(Mat[0][5])

# x=np.arange(8,30,0.001)
# y=f(x)

# plt.plot(x,y)
# plt.show()