# -*- coding: utf-8 -*-


import numpy as np
from pylab import *
from math import *

theta=[]
w=[]
t=[]

"""
input
"""

g=9.8 
l=1 
theta0=0 
theta.append(theta0)
w0=0 
w.append(w0)
t.append(0.0)
time=32*pi*sqrt(l/g)
dt=time/3000
F_D=float(input('F_D='))
Omega_D=float(input('Omega_D='))
q=float(input('q='))
'''
calculation
'''

for i in range(int(time/dt)):
    w.append(w[i]+dt*(-g/l*sin(theta[i])-q*w[i]+F_D*sin(Omega_D*t[i])))
    angle=theta[i]+dt*w[i+1]
    while angle>pi:
        angle=angle-2*pi
    while angle<-pi:
        angle=angle+2*pi
    theta.append(angle)
    t.append(t[i]+dt)
    print t[-1],theta[-1]
    

'''
plot 
'''
plot(t,theta,color='blue')
#legend(('nonlinear pendulum'),'lower left')
title('Nonlinear Pendulum ',fontsize=20)
xlabel('t(s)')
xlim(0,t[-1])
ylabel('theta(rad)')
show()
scatter(theta,w,s=1)
title('phase diagram',fontsize=20)
xlabel('theta(rad)')
ylabel('omega(rad/s)')
show()
