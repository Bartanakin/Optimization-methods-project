from mimetypes import init
from scipy.integrate import odeint
from scipy.integrate import quad
from scipy.optimize import minimize
from scipy.optimize import minimize_scalar
import numpy as np
import matplotlib.pyplot as plt
import constants as c
from math import factorial

# Module main

n = 4
init_a = np.array([ 2/factorial(n-i) for i in range(n) ])



def T(x: float, a: np.array):
    result = 0
    for i in range(len(a) - 1):
        result += a[i]
        result *= x
    result += a[-1]
    return result

def Do(x: float):
    return 110/c.x_c * x  # for 0 we count avarage speed 

def diff_count(y,x,a):
    dtdx =  np.sqrt(c.S)/np.sqrt( T(x,a) - Do(x) )
    return dtdx

def F(x: float, a: np.array):
    c.F_C*T(x,a)

def objective_function(a: np.array):
    return c.P_t*odeint(diff_count,0,[0,c.x_c],args = (a,))[1][0] +c. P_f*c.F_C*quad(T,0,c.x_c,args=(a,))[0]


contraints = []
contraints.append( {'type': 'ineq', 'fun': lambda a: minimize_scalar( lambda x: T(x,a) - Do(x), method='bounded',bounds=(0,c.x_c)).fun } )
contraints.append( {'type': 'ineq', 'fun': lambda a:  c.T_max + minimize_scalar( lambda x: -T(x,a), method='bounded',bounds=(0,c.x_c)).fun } )
result = minimize(objective_function,init_a,method='SLSQP',constraints=contraints)
print(result)
x = np.linspace(0,c.x_c,1000)
y = []
for i in range(1000):
    y.append(T(x[i],result.x))

plt.plot(x,y,'r-')
ax = plt.gca()
ax.set_xlim([0, c.x_c])
ax.set_ylim([0, c.T_max])
plt.ylabel('engine power')
plt.xlabel('distance')
plt.show()
