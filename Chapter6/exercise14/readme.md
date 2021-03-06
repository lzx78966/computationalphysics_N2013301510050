## problem 6.6

>##摘要
一维波动方程利用差分法来求解，验证在一根两端边界固定的弦在初始时刻给一个扰动，之后的过程中，产生的两个波包，在碰撞后，速度以及振幅不变的事实。

>##背景
对于波的运动，我们有波动方程:  
![1](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter6/exercise14/1.png)  
这个波动方程对于不同种类的波都是适用的，只需要把对x的求二次偏导相应修改一下即可。在本文中我只考虑一维弦上的波动。y代表弦上各点相对于其平衡位置的位移，x代表各点在弦上的坐标，t代表时间，c代表波在弦上的传播速度。

>##正文
我们考察初始时刻在弦上施加一个高斯型的干扰后，弦上波的传播情况。这里我们选择弦长为1m，c=300m/s，dx=0.01m，dt=dx/c。边界点固定。你可以在这里得到[代码](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter6/exercise14/problem6.6.1.py)。在弦上施加的干扰为:  
![2](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter6/exercise14/2.png)  
其中x0=0.3m，k=1000m^(-2)。弦上波的传播情况如下：  
![3](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter6/exercise14/3.gif)  
由图可知，高斯型的干扰变为了两个相反方向的波传播，这两个波的峰值为原干扰的一半。且当其传播到了边界点时，波峰变为波谷，波谷变为波峰，这直接对应于物理中的半波损失，即波从光疏介质传播到光密介质时相位会减少180°。
齐次线性偏微分方程的一个重要特征是有限个解的线性组合也是方程的解。由此，在弦上运动的两个波包的运动是独立的。为了说明这一点，我们在弦上的x=0.3m，0.7m处各施加一个峰值不同的高斯型扰动，观察之后波包的运动。你可以在这里得到[代码](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter6/exercise14/problem6.6.2.py)。得到的图像如下图所示：  
![4](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter6/exercise14/4.gif)  
由图可知，各个波之间没有相互干扰，其在“碰撞”前后的形状和速度均没有变化。由此可知，这几个波作为弦的运动的解，是相互独立的

>##结论
从上图中可以看出两个波包在碰撞到边界后，发生半波损失，振幅反向，且可以看出，两个波包在碰撞前后，相速以及振幅都不变，各自沿着原来的方向运动。

