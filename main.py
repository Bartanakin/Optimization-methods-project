from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

# Module main

n = 10
init_a = np.array([ 1 for i in range(n) ])
S = 1.2

def T(x: float, a: np.array):
    result = 0
    for i in range(len(a) - 1):
        result += a[i]
        result *= x
    result += a[-1]
    return result

def Do(x: float):
    return 0 # for 0 we count avarage speed 

def diff_count(y,x,a):
    dtdx =  np.sqrt(S)/np.sqrt( T(x,a) - Do(x) )
    return dtdx

def diff_test(y,x):
    dtdx = x**2
    return dtdx

y0 = 0
x = np.linspace(-40,40,1000)
y = odeint(diff_count, y0, x,args = (init_a,))

plt.plot(x,y,'r-',label='Output (y(t))')
plt.ylabel('time')
plt.xlabel('distance')
plt.legend(loc='best')
plt.show()