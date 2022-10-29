import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return (np.cos(x)-2*x)

def manual_derivative(x,h,precision_digits):
    if abs((f(x+h)-f(x))/h - (f(x+h/10)-f(x))/(h/10) ) / (f(x+h/10)-f(x))/(h/10) < 0.005 * pow(10, 2-precision_digits):

        return (f(x+h/10)-f(x))/(h/10)

    else:
        manual_derivative(x, h/10, precision_digits)


def newton_ralphson(x_guess, precision_digits, iteration_limit):
    x_preds=[]
    e=[]
    x_preds.append(x_guess)
    for i in range(0,iteration_limit):
        x_preds.append(x_preds[-1] - f(x_preds[-1]) /  (manual_derivative(x_preds[-1], 0.001, precision_digits)))

        e.append(abs(x_preds[-2]-x_preds[-1])/(x_preds[-1]))
        if abs(x_preds[-2]-x_preds[-1])/(x_preds[-1]) < 0.005 * pow(10, 2-precision_digits):
            break
    
    return x_preds,e,i



x,e,i=newton_ralphson(2,8,1000)

root=x[-1]

print("The Root of the Equation is ",root)

# x=np.arange(-5,5,0.001)
# y=f(x)

# plt.plot(x,y)
# plt.show()