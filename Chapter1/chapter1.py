# -*- coding: utf-8 -*-  

 #question1.5

 #初始化参数

print'Please Import Initial numbers and we can can go on: '

na_0=float(raw_input('The initial number of A: '))
nb_0=float(raw_input('The initial number of B: '))
t_0=float(raw_input('The initial number of time: '))
dt=float(raw_input('The time step is: '))
na=[na_0]
nb=[nb_0]
t=[t_0]

 #进行计算

for i in range(200):
    na_next=na[-1]+(nb[-1]-na[-1])*dt
    nb_next=nb[-1]+(na[-1]-nb[-1])*dt
    t_next=t[-1]+dt
    na.append(na_next)
    nb.append(nb_next)
    t.append(t_next)

 #画图

from pylab import *


aa=array(na)
bb=array(nb)
tt=array(t)

plot(tt,aa,label='NA',color='yellowgreen')
plot(tt,bb,label='NB',color='gold')

yticks([0,10,20,30,40,50,60,70,80,90,100])

plt.xlabel('time (s)')
plt.ylabel('The initial number')
plt.title('picture for question 1.5')
plt.grid(True)
plt.savefig("chapter1 picture.png")
plt.show()

