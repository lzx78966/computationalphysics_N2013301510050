from __future__ import division
from math import *
from pylab import *


def change_amp(F):
    q = 0.5
    l = 9.8
    g = 9.8
    f = 2/3
    dt = 0.04
    theta0 = 0.2
    omega0 = 0
    angle = [theta0]
    avelo = [omega0]
    t = [0]
    while t[-1] < 60:
        avelo_new = avelo[-1] - ((g/l)*sin(angle[-1]) + q*avelo[-1] - F*sin(f*t[-1]))*dt
        avelo.append(avelo_new)
        angle_new = angle[-1] + avelo[-1]*dt
        while angle_new > pi:
            angle_new -= 2*pi
        while angle_new < -pi:
            angle_new += 2*pi
        angle.append(angle_new)
        t_new = t[-1] + dt
        t.append(t_new)

    return angle,avelo,t

angle_0 = change_amp(0)[0]
avelo_0 = change_amp(0)[1]
t_0 = change_amp(0)[2]
angle_1 = change_amp(0.5)[0]
avelo_1 = change_amp(0.5)[1]
t_1 = change_amp(0.5)[2]
angle_2 = change_amp(1.2)[0]
avelo_2 = change_amp(1.2)[1]
t_2 = change_amp(1.2)[2]

plot(t_0,avelo_0,label='FD=0')
plot(t_1,avelo_1,label='FD=0.5')
plot(t_2,avelo_2,label='FD=1.2')

legend(loc='upper right')
title('angular velocity versus time')
xlabel('time(s)')
ylabel('omega(radians/s)')
xlim(0,60)
grid(True)



show()
