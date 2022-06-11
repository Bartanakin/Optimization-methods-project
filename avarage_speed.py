from scipy.optimize import minimize_scalar
import numpy as np
import matplotlib.pyplot as plt
import constants as c
from golden_search import golden_search

init_a = c.T_max/2

def objective_function(a: float):
    return c.P_t*np.sqrt(c.S)/np.sqrt(a)*c.x_c + c.P_f*c.F_C*c.x_c*a

# result = minimize_scalar(objective_function,init_a,method='bounded',bounds=(0.0001,c.T_max))
result_arg = golden_search(objective_function,0.00001,c.T_max)
result_value = objective_function(result_arg)
print(result_arg)
x = np.linspace(0.000001,c.T_max,1000)
y = objective_function(x)

plt.plot(x,y,'r-')
plt.plot([result_arg],[result_value],'-o',color='black')
plt.ylabel('cost')
ax = plt.gca()
ax.set_ylim([0, result_value*5])
plt.xlabel('engine power')
plt.show()