## problem 3.26

>##摘要
本文使用Euler法通过数值计算研究了Lorenz模型,并尝试使用Vpython进行了3D展示。

>##背景
我们之前已经讨论过单摆的混沌系统，尽管那是很简单的系统，但却表现出了极为丰富的行为，所以当我们考虑稍微复杂一点的系统时，该系统能够表现出混沌行为也就不那么让人奇怪了。习题3.26讨论的洛仑兹模型是研究流体力学的微分方程，而且讨论的是其中一种特殊情况——瑞利—伯纳德模型。洛仑兹模型如下图所示：  
![lorenz](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter3/exercise10/Lorenz.gif)  
该模型可以概括为一个三元的微分方程组：  
![1](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter3/exercise10/1.png)  

>##正文
接下来我们考察Lorenz模型的行为。我们令sigma=10，b=8/3，改变r的大小，观察z随时间的变化情况（x与y将呈现相似的行为）。在这个模型中，r代表了流体顶部与底部的温度差，类似于单摆问题中外界驱动力的地位。此处不涉及二阶微分，故euler法就可以保证运算在一定程度下的准确性， 分别讨论了r=5,10,25的情形，做出z（t）图像.你可以在这得到[代码](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter3/exercise10/problem3.26.1.py)。以下是各情况的图像对比：  
![2](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter3/exercise10/2.png)  
由图可知，当r=5时，图像一开始有一点振荡，随后振幅衰减，z变成一个与时间无关的常数。当r=10时，图像的特征相似，只是振幅衰减所花的时间要更长一些。这两种情况对应于流体中的稳定对流运动。它类似于非混沌单摆的运动模式。当r=25时，图像最终变为混沌状态。
理论计算发现出现混沌现象的r的临界值为470/19=24.74,图像显示结过与此吻合。参照前面研究单摆混沌系统的方法，我们可以做出x-z的相空间图像，可以发现轨迹随r的变化，即无混沌到混沌的变化十分显著。你可以在这里得到[代码](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter3/exercise10/problem3.26.2.py)。  
![3](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter3/exercise10/3.png)  
![4](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter3/exercise10/4.png)  
![5](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter3/exercise10/5.png)  
由图可知，当系统处于非混沌状态时，其轨迹最终会收缩到相空间中的一个点，即代表系统处于稳定状态。而混沌系统中，轨迹呈现出某种周期性,与混沌摆的情况类似，出现了奇异吸引子。由于它们出现在Lorenz模型中，习惯上被称为Lorenz吸引子。
Lorenz吸引子的三维图示如图，你可以在这里得到[代码](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter3/exercise10/problem3.26.3.py).
![6](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter3/exercise10/6.png)  
Lorenz吸引子在三维相空间中形成的动态图如图，你可以在这里得到[代码](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter3/exercise10/problem3.26.4.py)。  
![gif](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter3/exercise10/gif1.gif)  
进一步的，我们取这根三维曲线在x=0平面与y=0平面所截出的图像，可以发现即使该系统是高度混沌的，但是相空间中的吸引子表面还是体现很好的规律性的，并且是独立于初始条件的。 你可以在这里得到[代码](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter3/exercise10/problem3.26.5.py)，图像如下所示：  
![7](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter3/exercise10/7.png)  
  

>##结论
相空间中的吸引子图像与初值条件无关，即混沌系统中在某些参数确定后相对规则的一部分。


