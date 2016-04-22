##problem 3.4

>##摘要
简谐振动与非简谐振动的周期关系。

>##题目背景
简谐振动的微分方程的一般形式加以拓展，即：![picture1](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter3/picture1.gif)  
对幂次分别为1和3时进行讨论,为了方便，k=1，其中alpha=1时，对应简谐振动的情况，alpha=3为非简谐振动的情况。探究两者振幅与周期的关系。

>##正文
由于使用euler法会使每一步的系统能量不断增加，导致单方向累计的较大误差，故这里采用euler-cromer法对原有的算法做一点小小的修改，即在计算下一个时刻的位置是使用下一个时刻的速度，这样的改动可使每一步的误差得到控制。具体操作如下：  
![picture2](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter3/picture2.png)  
你可以在这里得到我的代码。[代码](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter3/problem3.4.py)  
在简谐振动中，所得图像为：  
![picture5](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter3/picture5.png)
在非简谐情况中，所得图像为：   
![picture6](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter3/picture6.png)  

>##结论
经过观察，可以发现，在简谐振动中，运动周期与振幅大小无关(此处振幅的大小取决于初速度)，而非简谐振动的情况下，振幅越小，振动周期越大，即两者是存在某种联系的。 对于简谐振动而言![picture7](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter3/picture7.png).而对于这里的非简谐振动，通过maple解得解析解为Jacobi正弦函数:  
![picture3](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter3/picture3.png)  
下面是关于雅可比正弦函数的一些介绍:  
![picture4](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter3/picture4.png)  
从上式可以看出该函数的振幅的确与周期有函数关系，并且由图像模拟可知，振幅越小，周期越长。

##problem3.12

>##摘要
混沌系统。

>##背景
物理摆在加了阻尼与周期性的驱动力之后，当周期性的驱动力的最大值F_d达到一定值时，产生了不可预测的轨迹，然而当F_d较小时，其运动状况又是可以预测的，这就是一个混沌系统所具备的条件。

>##正文
本次计算依然使用euler-cromer法，所用的微分方程组为：  
<center>![1](<a href="https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter3/picture4.png" rel="nofollow">https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter3/picture4.png</a>)  
<center>![2](<a href="https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter3/picture4.png" rel="nofollow">https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter3/picture4.png</a>)  
用子程序形式即为：  
<center>![3](<a href="https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter3/picture4.png" rel="nofollow">https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter3/picture4.png</a>)  
<center>![4](<a href="https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter3/picture4.png" rel="nofollow">https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter3/picture4.png</a>)  
<center>![5](<a href="https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter3/picture4.png" rel="nofollow">https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter3/picture4.png</a>)

你可以在这里得到我的[代码]()  
所得F_d在各种取值下theta的图像  
!(6)[]  
!(7)[]  
!(8)[]  
由于在F_d较大的情况下，混沌系统的运动状况无法预测，且角度与时间的图像不够直观，所以绘制相图theta-omega:  
!(9)[]  
!(10)[]  
绘出在特定的时间节点形成奇异吸子构成的相图，并与书中所给的pi/2的情况做对比:
!(11)[]  
以下是pi/2的情况，即驱动力最大的点 :
!(12)[]  
接着是pi/4的情况:  
!(13)[]  

>##结论
取不同的时间节点绘制出的吸相图是不同的，具备一定的分形结构，在细节出的图像与图像的整体形貌是一致的。

