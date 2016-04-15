##problem 3.4

>##摘要
简谐振动与非简谐振动的周期关系。

>##题目背景
简谐振动的微分方程的一般形式加以拓展，即：![picture1](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter3/picture1.gif)  
对幂次分别为1和3时进行讨论,为了方便，k=1，其中$alpha$=1时，对应简谐振动的情况，$\alpha$=3为非简谐振动的情况。探究两者振幅与周期的关系。

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
