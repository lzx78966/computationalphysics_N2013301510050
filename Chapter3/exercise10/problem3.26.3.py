import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# define the positions of z, r is variable
def phase(r):
    x=[1]
    y=[0]
    z=[0]
    dxdt=[0]
    dydt=[0]
    dzdt=[0]
    t=[0]
    dt=0.0001
    sigma=10
    b=8/3
    for i in range(499999):
        dxdt.append(sigma*(y[-1]-x[-1]))
        dydt.append(-x[-1]*z[-1]+r*x[-1]-y[-1])
        dzdt.append(x[-1]*y[-1]-b*z[-1])
        x.append(x[-1]+dxdt[-1]*dt)
        y.append(y[-1]+dydt[-1]*dt)
        z.append(z[-1]+dzdt[-1]*dt)
        t.append(t[-1]+dt)
    return x,y,z

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.plot(phase(25)[0],phase(25)[1],phase(25)[2])
plt.title('Phase space plot')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()
