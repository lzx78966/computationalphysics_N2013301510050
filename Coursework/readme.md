<h1 align = "center">结课论文</h1>

<h2 align = "center">从单摆到混沌现象</h2>

###摘要：
利用python软件强大的数值计算功能,严格求解无阻尼单摆和有阻尼单摆的运动方程,研究单摆摆长,阻尼系数和初始摆角对单摆运动的影响.研究结果表明:单摆的周期与初始摆角有关,单摆周期随初始摆角的增大而增大;当两种单摆的参数取值处于某些范围时,均能出现混沌现象;阻尼单摆在正阻尼条件下演化出随机吸引子,在负阻尼条件下演化出随机排斥子.通过计算不同参数值的单摆方程,发现单摆的运动对初始摆角、阻尼系数有很强的依赖性.并对阻尼单摆在正阻尼条件下的吸引子做了相关研究。
###关键词：
python;单摆;混沌;吸引子

###正文
* [1.单摆简介](#1)
	* [1.1.无阻尼的单摆](#1.1) 
	* [1.2.有阻尼的单摆](#1.2) 
* [2.混沌简介](#2) 
	* [2.1.混沌的特征](#2.1) 
* [3.单摆的混沌运动](#3) 
	* [3.1.混沌摆对初始条件的敏感性](#3.1) 
	* [3.2.混沌摆角度与初始角速度的关系验证](#3.2) 
	* [3.3.简谐运动到混沌运动的影响因素](#3.3) 
* [4.奇异吸引子简介](#4) 
	* [4.1.影响奇异吸引子的因素探究](#4.1)  

<h4 id="1">1.单摆简介</h4>  
单摆Simple pendulum，是由一根不会伸缩的细线或细棒和一个很小的重球所构成的振动系统。用一根绝对挠性且长度不变、质量可忽略不计的线悬挂一个质点，在重力作用下在铅垂平面内作周期运动，就成为单摆。  
![1](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Coursework/1.gif)  
<h5 id="1.1">1.1.无阻尼的单摆</h5>  
![2](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Coursework/2.jpg)  
如图所示，忽略细绳重量，也不计小球受到的空气阻力，则上诉单摆可看成理想单摆。单摆的运动方程可表达为：  
![3](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Coursework/3.png)  
这是一个非线性二阶常微分方程。若单摆仅在其平衡位置（θ=0）附近作微摆动，|θ| <<1，sinθ ≈ θ，此单摆方程可线性化为标准的线性单振子方程，而ω0 正是单摆作线性摆动的固有频率，2π/ ω0是摆动周期。也就是线性的单摆，但是，如果摆角|q|<<1的条件不满足，则sinq不能用q 取代，线性化无效，必须求解单摆非线性方程,也就是非线性的单摆。下面给出无阻尼状态下线性单摆与非线性单摆的轨迹比较与相图比较。  
初始角度为10degree时：  
[![11](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Coursework/11.png "title")](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Coursework/1.py) 
初始角度为179degree时：  
[![11.1](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Coursework/11.1.png "title")](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Coursework/1.py)
相图比较：  
[![11.2](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Coursework/11.2.png "title")](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Coursework/1.py)  

<h5 id="1.2">1.2.有阻尼的单摆</h5>  
无阻尼的单摆考虑的是理想情况，但在实际生活中我们还要考虑到空气阻力等一系列阻力对单摆运动的影响，也就是有阻尼的单摆。在无外界驱动力有阻尼的情况下，单摆的振动方程可以进行改写：  
![4](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Coursework/4.png)  
显然，第一个方程只是原来的运动方程的改动版，在等号右侧加入了阻尼项。阻尼项之所以正比于角速度，是因为实验上发现阻力一般与物体的速度成反比关系。第二个方程是弱阻尼情况下的振动方程，第三个是过阻尼情况下的方程，第四个是临界阻尼情况下的方程。下图给出不同阻尼项的单摆角度比较：  
[![12](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Coursework/12.png "title")](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Coursework/2.py)  
如果是有外力驱动的有阻尼单摆，考察此时的单摆运动。因为所有的外力的函数可以分解为若干正弦函数的组合，故我在此假设外力是正弦函数形式。这样单摆的动力学方程可以写成:  
![6](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Coursework/6.png)  
显然，单摆最终做正弦运动，其振幅由单摆固有频率，外力频率和阻尼系数共同决定，其频率等于外力的频率。下图是其角度变化图：  
[![13](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Coursework/13.png "title")](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Coursework/3.py)  

<h4 id="2">2.混沌简介</h4>  

<h5 id="2.1">2.1.混沌的特征</h5>  

<h4 id="3">3.单摆的混沌运动</h4>  

<h5 id="3.1">3.1.混沌摆对初始条件的敏感性</h5>  

<h5 id="3.2">3.2.混沌摆角度与初始角速度的关系验证</h5>  

<h5 id="3.3">3.3.简谐运动到混沌运动的影响因素</h5>  

<h4 id="4">4.奇异吸引子简介</h4>  

<h5 id="4.1">4.1.影响奇异吸引子的因素探索</h5>










###结论

###致谢（参考文献）

