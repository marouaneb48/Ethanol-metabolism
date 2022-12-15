import matplotlib.pyplot as plt
import numpy as np
import math
import sys
sys.setrecursionlimit(100000)



## état continu 
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


##hybride version 1

C0 = 1 # Concentration initiale totale
Ve = 0.5
Vs = 5
k1 = 0.16
k2 = 0.0000725
T = 5 # Temps régulier de consommation (min)
T_max = 200 # Durée de consommation (min)

def f(t):
    return max(0,C0*(T/T_max)*Ve/Vs*(1-math.exp(-k1*t)) - k2*t) + f(t-T) if t >= 0 else 0  # "C0*T/T_max" pour dire que l'alcoolique prend une dose régulière

line1, = plt.plot(np.linspace(0,T_max,1000),list(map(f,np.linspace(0,T_max,1000))))
T = 10
line2, = plt.plot(np.linspace(0,T_max,1000),list(map(f,np.linspace(0,T_max,1000))),"g")
T = 50
line3, = plt.plot(np.linspace(0,T_max,1000),list(map(f,np.linspace(0,T_max,1000))),"r")
plt.legend((line1, line2, line3), ('T = 5min', 'T = 10min', 'T = 50 min'))
plt.ylabel('Concentration (mol/L)')
plt.xlabel('Temps (min)')
plt.show()


## hybride version 2 (infini)
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