# -*- coding: utf-8 -*-

import numpy as np
from pylab import *
from math import *

theta_last=[]
FD=[]

def bifurcation(F_D):
    theta=[]
    w=[]
    t=[]
    g=9.8 
    l=1 
    theta0=0 
    theta.append(theta0)
    w0=0 
    w.append(w0)
    Omega_D=2.0 
    q=1 
    t.append(0.0)
    n=400
    m=2000
    time=n*2*pi/Omega_D
    dt=time/n/m
    for i in range(int(time/dt)):
        w.append(w[i]+dt*(-g/l*sin(theta[i])-q*w[i]+F_D*sin(Omega_D*t[i])))
        angle=theta[i]+dt*w[i+1]
        while angle>pi:
            angle=angle-2*pi
        while angle<-pi:
            angle=angle+2*pi
        theta.append(angle)
        t.append(t[i]+dt)

    print theta[-1]
    return theta[-1]

for i in range(1500):
    F_D=6+i*0.001
    FD.append(F_D)
    theta_last.append(bifurcation(F_D))


scatter(FD,theta_last,s=1)
title('bifurcation diagram',fontsize=15)
xlabel('F_D')
xlim(6,7.5)
ylabel('theta(rad)')
show()
