import matplotlib.pyplot as plt
import numpy as np
import math
import sys
sys.setrecursionlimit(100000)

C0 = 0.02
Ve = 0.5
Vs = 5
k1 = 0.16
k2 = 0.0000725
T = 20 # Temps régulier de consommation (min)
T_max = 90 # Durée de consommation (min)

def f(t):
    return max(0,C0*Ve/Vs*(1-math.exp(-k1*t)) - k2*t) + f(t-T) if t >= 0 else 0

line1, = plt.plot(np.linspace(0,T_max,1000),list(map(f,np.linspace(0,T_max,1000))))
T = 5
line2, = plt.plot(np.linspace(0,T_max,1000),list(map(f,np.linspace(0,T_max,1000))),"g")
T = 1
line3, = plt.plot(np.linspace(0,T_max,1000),list(map(f,np.linspace(0,T_max,1000))),"r")
plt.legend((line1, line2, line3), ('T = 20min', 'T = 5min', 'T = 1 min'))
plt.ylabel('Concentration (mol/L)')
plt.xlabel('Temps (min)')
plt.show()