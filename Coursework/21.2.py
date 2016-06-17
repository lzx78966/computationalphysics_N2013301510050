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
    while t[-1] < 300:
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


angle_1 = change_amp(1.2)[0]
avelo_1 = change_amp(1.2)[1]



scatter(angle_1,avelo_1)



title('angular velocity versus angle when F=1.2')
xlabel('theta(radians)')
ylabel('omega(radians/s)')

grid(True)



show()
