from mimetypes import init
from scipy.integrate import odeint
from scipy.integrate import quad
from scipy.optimize import minimize
import numpy as np
import matplotlib.pyplot as plt

# Module main

n = 1
init_a = np.array([ 1 for i in range(n) ])
S = 1.2
P_t = 100
P_f = 100
F_C = 100
x_c = 40
T_max = 100


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

def F(x: float, a: np.array):
    F_C*T(x,a)

def objective_function(a: np.array):
    return P_t*odeint(diff_count,0,[0,x_c],args = (a,))[1][0] + P_f*F_C*quad(T,0,x_c,args=(a,))[0]

contraints = []
N = 100
delta = x_c/N
for i in range(N + 1):
    contraints.append( {'type': 'ineq', 'fun': lambda a: T(delta*i,a) - Do(delta*i)} )
    # contraints.append( {'type': 'ineq', 'fun': lambda a: T_max - T(delta*i,a)} )
result = minimize(objective_function,init_a,method='SLSQP',constraints=contraints)
print(result)
x = np.linspace(0,x_c,1000)
y = []
for i in range(1000):
    y.append(T(x[i],result.x))

print(objective_function(np.array([0.001])))
plt.plot(x,y,'r-')
plt.ylabel('engine power')
plt.xlabel('distance')
plt.show()