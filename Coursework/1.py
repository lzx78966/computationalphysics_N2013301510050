import numpy as np
from pylab import *
from math import *

theta=[]
w=[]
t=[]
the_lin=[]
w_lin=[]


g=9.8 
l=1 
theta0=pi*float(input('theta0(degree)='))/180
theta.append(theta0)
w0=float(input('omega0(rad/s)='))
w.append(w0)
t.append(0.0)
time=16*pi*sqrt(l/g)
dt=float(input('time step='))
the_lin.append(theta0)
w_lin.append(w0)



for i in range(int(time/dt)):
    w.append(w[i]+dt*(-g/l*sin(theta[i])))
    theta.append(theta[i]+dt*w[i+1])
    t.append(t[i]+dt)
    w_lin.append(w_lin[i]+dt*(-g/l*the_lin[i]))
    the_lin.append(the_lin[i]+dt*w_lin[i+1])
    print t[-1],theta[-1],the_lin[-1]
    


plot(t,theta,color='blue')
plot(t,the_lin,color='red')
legend(('nonlinear pendulum','linear pendulum'),'lower left')
title('Nonlinear Pendulum and Linear Pendulum',fontsize=20)
xlabel('t(s)')
xlim(0,t[-1])
ylabel('theta(rad)')
show()

plot(w,theta,color='blue')
plot(w_lin,the_lin,color='red')
legend(('nonlinear pendulum','linear pendulum'),'upper right')
title('phase diagram',fontsize=20)
xlabel('omega(rad/s)')
ylabel('theta(rad)')
show()
