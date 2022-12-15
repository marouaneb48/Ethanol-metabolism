import matplotlib.pyplot as plt
import numpy as np
import math
import sys
sys.setrecursionlimit(100000)

C0 = 0.05
Ve = 0.5
Vs = 5
k1 = 0.16
k2 = 0.0000725
T_max = 120

def f(t):
    return max(0,C0*Ve/Vs*(1-math.exp(-k1*t)) - k2*t)

line1, = plt.plot(np.linspace(0,T_max,1000),list(map(f,np.linspace(0,T_max,1000))))
C0 = 0.1
line2, = plt.plot(np.linspace(0,T_max,1000),list(map(f,np.linspace(0,T_max,1000))),'g')
C0 = 0.25
line3, = plt.plot(np.linspace(0,T_max,1000),list(map(f,np.linspace(0,T_max,1000))),'r')
plt.legend((line1, line2, line3), ('C_0 = 0.05 mol/L', 'C_0 = 0.1 mol/L', 'C_0 = 0.25 mol/L'))
plt.ylabel('Concentration (mol/L)')
plt.xlabel('Temps (min)')
plt.show()