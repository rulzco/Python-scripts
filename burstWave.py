# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 15:27:03 2020

@author: ruloz
"""
#Square wave with base frequency, burst frequency and duty cycle.
import numpy as np
import matplotlib.pyplot as plt
f_b = 5 # Hz
f = 2e3 # Hz
T = 1.0 # s
dt = 1e-4 # s
duty = 0.5 
cycles = T * f_b
t = np.arange(0,1,dt)
y = np.ones(len(t))
t_t = 1 / f_b
t_on = duty / f_b
t_off = 1 / f_b * (1 - duty)
temp = 0
t_on_f = t_on * len(t)
t_t_f =  t_t * len(t)
for i in range(int(cycles)):
    k = i + 1
    y[int(temp + t_on_f + 1):int(k * t_t_f)] = 0 #temp + t_on to n-t_t, y[200:400]
    temp = temp + t_t_f
temp=0

yy = np.zeros(len(y))
for i in range(len(y)):
    if y[i] > 0:
        yy[i] = np.sin(2*np.pi*f*t[i])
    
plt.figure(3, figsize=(8, 6), dpi=90, facecolor='w', edgecolor='w')
plt.plot(t,yy,'--^',c='darkcyan',linewidth=1,markersize=1)
plt.legend(['$f_{base}$=  %a $Hz$ \n $F_{burst}$= %a $Hz$' %(f, f_b)])
plt.xlabel('Tiempo (s)')
plt.ylabel('V')
plt.title('Ciclo de trabajo %a' %(duty))
plt.grid(True)