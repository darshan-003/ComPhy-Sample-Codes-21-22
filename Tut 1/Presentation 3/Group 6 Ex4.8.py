import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sc

def h(x):
    return x/((1+x)**4)

# First Job is to Plot the function to see if we can even expect a finite answer
# Since the function aproaches 0 as it tends to infinity , we have a possibility of a finite answer
# Now Lets Apply the required Transformation
def k(y):
    return h(y/(1-y))


def f(y):
    return 1/(1-y)**2 * k(y)
# Now lets plot the Transformed function between Limits 0 to 1


x=np.arange(0,1,0.0001)
y=f(x)

plt.plot(x,y)
plt.show()

# Now Lets Calculate the integrals using various Methods

# First Using the avg of the function . Error scales as O(1/sqrt(n))
def Integralbyavg(a,b,n):
    sum=0
    for i in range(0,n):
       xi=np.random.uniform(a,b)
       sum+=f(xi)
        

   
    return (b-a)*sum/n


print(Integralbyavg(0,1,10000))


# Next Using the Gauss Lengendre Polynomials

def p(x,a,b): 
   return f(((b+a)+(b-a)*x)/2)






def gaussLegendreofgivenDegree(deg,a,b):
    xi,wi=sc.roots_legendre(deg)
    ans=0
    for i in range(0,deg):
        ans+=wi[i]*p(xi[i],a,b)

    return(ans*(abs(a-b)/2))




print(gaussLegendreofgivenDegree(3,0,1))


# So Using 2 different methods we get that the answer is 0.166666....

def q(x):
    return np.exp(x)*h(x)





# The final Confirmation can be obtained by using Gauss Laugree Polynomial Method on the Orignal Polynomial
def gaussLaugreeOfaGivenDegree(deg):
    xi,wi=sc.roots_laguerre(deg)
    ans=0
    for i in range(0,deg):
        ans+=wi[i]*q(xi[i])

    return ans
    
print(gaussLaugreeOfaGivenDegree(150))
