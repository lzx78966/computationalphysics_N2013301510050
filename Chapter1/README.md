##Question 1.5:

Consider again a decay problem with two types of nuclei A and B, but now suppose that nuclei of type A decay into ones of type B, while nuclei of type B decay into ones of type A. Strictly speaking, this is not a "decay" process, since it is possible for the type B nuclei to turn back into type A nuclei. A better analogy would be a resonance in which a system can tunnel or move back and forth between two states A and B which have equal energies. The corresponding rate equations are  ![公式一](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter1/1.png?raw=true)where for simplicity we have assumed that the two types of decay are characterized by the same time constant, tau. Solve this system of equation for the numbers of nuclei, NA and NB, as functions of time. Consider different initial conditions, such as NA=100, NB=0, etc, and take tau=1s. Show that your numerical results are consistent with the idea that the system reaches a steady state in which NA and NB are constant. In such a steady state, the time derivatives dNA/dt and dNB/dt should vanish.

##Solving process:

用差分代替题目中的微分可得：  
![公式二](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter1/2.png?raw=true)  
整理上式可以得到：  
![公式三](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter1/3.png?raw=true)

##Main process

>1.首先要初始化代码中我们需要的参量和变量  
>2.做计算得到NA，NB和时间的系列值  
>3.得出NA，NB和时间的值后，借助matplotlib去画出图像  
>4.得出图像后进行与理论的验证  

##Code  
 #question1.5  

 #初始化参数  
 print 'Import Initial numbers and we can go on:'  
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

你能在我的作业文件夹中得到这些代码。[chapter1 code](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter1/chapter1.py)

得到的函数图像如下![picture](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter1/chapter1picture.png?raw=true)
