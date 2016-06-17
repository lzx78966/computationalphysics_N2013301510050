<h1 align = "center">结课论文</h1>

<h2 align = "center">从单摆到混沌现象</h2>

###摘要：
利用python软件强大的数值计算功能,严格求解无阻尼单摆和有阻尼单摆的运动方程,研究单摆摆长,阻尼系数和初始摆角对单摆运动的影响.研究结果表明:单摆的周期与初始摆角有关,单摆周期随初始摆角的增大而增大;当两种单摆的参数取值处于某些范围时,均能出现混沌现象;阻尼单摆在正阻尼条件下演化出随机吸引子,在负阻尼条件下演化出随机排斥子.通过计算不同参数值的单摆方程,发现单摆的运动对初始摆角、阻尼系数有很强的依赖性.并对阻尼单摆在正阻尼条件下的奇异吸引子做了相关研究。
###关键词：
python;单摆;混沌;奇异吸引子

###正文
* [1.单摆简介](#1)
	* [1.1.无阻尼的单摆](#1.1) 
	* [1.2.有阻尼的单摆](#1.2) 
* [2.混沌简介](#2) 
	* [2.1.混沌的特征](#2.1) 
* [3.单摆的混沌运动](#3) 
	* [3.1.混沌摆对初始条件的敏感性](#3.1)  
	* [3.2.简谐运动到混沌运动的影响因素](#3.2) 
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
![7](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Coursework/7.jpg)  
现代科学所讲的混沌，其基本含义是说混沌轨道的运动完全受规律支配，但相空间中轨道运动不会中止，在有限空间中永远运动着，不相交也不会闭合。混沌运动表观上是无序的，产生了类随机性，也称内在随机性。非线性科学中的混沌现象指的是一种确定的但不可预测的运动状态，他的外在表现和纯粹的随机运动很相似，即都不可预测。但和随机运动不同的是，混沌运动在动力学上是可以确定的，它的不可预测性是来源于运动的不稳定性。或者说混沌系统对无限小的初值变动和微扰也具有敏感性，无论多小的扰动在长时间以后，也会使系统彻底偏离原来的演化方向。

<h5 id="2.1">2.1.混沌的特征</h5>  
1.系统方程无任何随机因子，但必须有非线性项  
混沌是决定性力学系统中出现的一种貌似随机的运动。所谓"决定性"是指描述系统运动状态的方程是确定的，不包含随机变量。要产生混沌运动，则确定性方程一定是非线性的。  
2.系统的随机行为是其内在特征，不是外界引起的。  
随机性可分为有外界施加的外在随机性和动力学系统本身所固有的内在随机性两种。实际上内在随机并不是一种真正的随机，她的行为是完全正确的，只是表现的太复杂，不可预测，就像是随机一样，这种混乱，随机是系统的一种内在特征。  
3.对初始条件极端敏感。  
内在随机性是通过对初始条件的极端敏感性表现出来的，初始条件的误差在非线性动态系统中可能会按指数规律增长。处于混沌状态的系统，运动轨迹将敏感的依赖初始条件，从两个及其邻近的初值出发的两轨道，在足够长的时间以后，必然会呈现出显著的差别来。再小的误差经系统各部分之间的非线性相互作用都可能被迅速放大，初始状态的信息很快消失，从而表现为行动的不可预测，这就是混沌运动。  

一般地，如果一个接近实际而没有内在随机性的模型仍然具有貌似随机的行为，就可以称这个真实物理系统是混沌的。一个随时间确定性变化或具有微弱随机性的变化系统，称为动力系统，它的状态可由一个或几个变量数值确定。而一些动力系统中，两个几乎完全一致的状态经过充分长时间后会变得毫无一致，恰如从长序列中随机选取的两个状态那样，这种系统被称为敏感的依赖于初始条件，而对初始条件的敏感的依赖性也可作为混沌的一个定义。

<h4 id="3">3.单摆的混沌运动</h4>  
单摆做混沌运动有如下主要特征：  
1.单摆产生混沌行为是以在大振幅条件下，动力学方程中含有非线性项为前提。  
2.单摆的混沌运动是一种确定性的随机行为。  
3.单摆的混沌运动有其内在规律性。  
4.单摆的混沌行为可以通过参量的改变进行控制。
下面给出混沌运动与非混沌运动的相图比较。  
下图是非混沌运动的相图：  
[![21.1](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Coursework/21.1.png 'title')](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Coursework/21.1.py)
下图是混沌运动的相图：  
[![21.2](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Coursework/21.2.png 'title')](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Coursework/21.2.py)  


<h5 id="3.1">3.1.混沌摆对初始条件的敏感性</h5>  
1,外力幅度。  
在综合考虑了能量耗散、外力驱动和非线性之后，物理摆的运动方程可以写作：  
![8](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Coursework/8.png)  
接下来我选择重力加速度和摆长均为9.8，阻尼系数为0.5，外力频率为2/3，时间间隔为0.04.分别对外力幅度为0、0.5、1.2的情况绘制摆的角度与时间的关系图如下：  
[![31.1](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Coursework/31.1.png 'title')](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Coursework/3.1.py)  
图中蓝色线表示外力为零的状态，可见没有外界驱动力下的单摆在阻力的影响下很快就停止了。图中绿线表示外力幅度为0.5时的运动，可见单摆在开始阶段将初始条件决定的运动通过阻力消耗后，在之后的运动中做与外力同频率的简谐振动。这两种单摆的运动与上一篇文章中描述的一样。红色的线表示外力幅度为1.2时的运动状态，可以看到，单摆的运动是没有周期性的，这就是混沌的特征。  
下图是角速度的变化情况：  
[![31.2](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Coursework/31.2.png 'title')](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Coursework/3.2.py)  
由上图可见，三种单摆的角速度的变化特征与上面所述的角度的变化特征相似。这是显然的，因为角速度只不过是角度对时间的导数罢了。  
2.初始角度。  
混沌摆的最大特征是当初值仅仅改变了一点点时，结果就会有极大的变化。为了示意这种情况，我选择两个摆，它们的初始角度仅仅相差0.001rad。先观察F=1.2,即混沌状态下角度之差的变化如下图：  
[![31.3](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Coursework/31.3.png 'title')](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Coursework/3.3.py)  
可以明显看出，在混沌状态下，初始角度相差极小的两个物理摆的角度差随着时间推移会变大，最终趋于稳定，这种稳定是因为已经达到可能的最大差2pi。这表明混沌摆对初值敏感性很强。  
接下来观察F=0.5，即非混沌状态下角度之差的变化如下图：  
[![31.4](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Coursework/31.4.png 'title')](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Coursework/3.4.py)  
从中可以看到，对于两个初始位置差异很小的非混沌摆，其角度差会迅速减小，最终趋于0.这表明非混沌摆对初值不敏感。  

<h5 id="3.2">3.2.简谐运动到混沌运动的影响因素</h5>  
接下来我们研究单摆系统是如何从简谐振动变为混沌振动的。为了更好地研究这一渐变过程，我们画所谓的bifurcation图。所谓bifurcation图，图上的点对应的是外力相位为零的时刻。如图所示为bifurcation图:  
[![32.1](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Coursework/32.1.png 'title')](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Coursework/32.1.py)  
由图可知，从1.35开始的一段中，每一个F只对应一个角度，这时单摆的周期与外力周期一致。之后每个F对应两个角度，表明其周期是外力两倍。以后周期逐渐变为外力周期的四倍、八倍等。由于分辨率的问题，图中难以显示更长周期的情况，但是显然的是，当F持续增大后，周期会越来越长，最终进入没有周期的混沌情况。

改变参数对bifurcation图的影响  
接下来研究的是改变外力频率和阻尼系数时bifurcation图会有什么变化。即影响混沌运动的因素探究。  
首先改变外力的频率，令f=2/3,2/3+0.00001,2/3+0.00002,结果如下图:  
[![32.2](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Coursework/32.2.png 'title')](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Coursework/32.2.py)  
由图可知，当外力的频率增大时，图像的结构没有发生变化，只是图形整体下移，且上面的点有所增加。  
其次改变阻尼系数，令q=0.5,0.51,0.52，结果如下图:  
[![32.3](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Coursework/32.3.png 'title')](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Coursework/32.3.py)  
由图可知，当阻尼系数有微小的变化时，图像整体右移，亦即推迟了混沌现象的出现。

<h4 id="4">4.奇异吸引子简介</h4>  
奇异吸引子是反映混沌系统运动特征的产物，也是一种混沌系统中无序稳态的运动状态。它又称为混沌吸引子，它具有复杂的拉伸，扭曲的结构。奇异吸引子是系统总体稳定性和局部不稳定性共同作用的产物，它具有自相似性，具有分形结构。  
奇异吸引子是混沌运动的主要特征之一。奇异吸引子的出现与系统中包含某种不稳定性（不同于轨道不稳定性和李雅普诺夫不稳定性）有着密切关系，它具有不同属性的内外两种方向：在奇异吸引子外的一切运动都趋向（吸引）到吸引子，属于“稳定”的方向；一切到达奇异吸引子内的运动都互相排斥，对应于“不稳定”方向。  
奇异吸引子具有两个主要的特点：①奇异吸引子上的运动对初始值表现出极强的敏感依赖性，在初始值上的微不足道的差异，就会导致运动轨道的截然不同。②奇异吸引子往往具有非整数维.  
下图给出的是上文中讨论的混沌摆的奇异吸引子图像：  
[![41.1](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Coursework/41.1.png "title")](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Coursework/41.1.py)  
如果是非混沌情况，图中只会有一个点。而在混沌情况中图中会出现奇异吸引子。

<h5 id="4.1">4.1.影响奇异吸引子的因素探索</h5>
在上文中的奇异吸引子的图中，我们取的是外力相位为0的时刻。在这里，我们探究一下取别的相位为基准时，奇异吸引子有什么变化。  
首先是时间取值是外力相位为+pi/2的时刻的奇异吸引子图像：  
[![41.2](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Coursework/41.2.png "title")](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Coursework/41.2.py)  
再是时间取值是外力相位为+pi/4的时刻的奇异吸引子图像：  
[![41.3](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Coursework/41.3.png "title")](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Coursework/41.3.py)  
由这两张图连同上文中的一张图可以看出，这里明显随着相位从0到pi/4再到pi/2,奇异吸引子先向右上方、再向右下方运动。这表明随着相位的变化，奇异吸引子也相应的运动。  
接下来我们探究当参数有微小变化时奇异吸引子的变化情况。我们选择外力的幅度和频率作为参数，分别令幅度F=1.2，1.25,1.3和f=2/3,2/3+0.00001,2/3+0.00002，观察奇异吸引子的变化。  
首先是幅度变化时奇异吸引子的对比：  
[![41.4](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Coursework/41.4.png "title")](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Coursework/41.4.py)  
由这三张图可以看出，当F增加时，奇异吸引子的位置没有发生改变，但其上的点逐渐减少，这表明系统在逐渐离开混沌状态 。  
之后是频率变化时奇异吸引子的对比：  
[![41.5](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Coursework/41.5.png "title")](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Coursework/41.5.py)  
由这三张图可以看出，当外力频率每次以0.00001的大小增加时，奇异吸引子的位置基本没变，但其上的点逐渐增加，吸引子的在相空间中体积增大，表明其“吸引”能力在逐渐下降。

###结论
通过经过python语言的数值计算，我得到了以下结论：  
1.摆角的增大使单摆分为线性单摆和非线性单摆;当有阻尼和无阻尼单摆的参数取值处于某些范围时,均能出现混沌现象。并通过对不同初始角度的线性与非线性轨迹进行了比较,验证了单摆的周期与初始摆角有关,单摆周期随初始摆角的增大而增大.  
2.讨论了混沌运动的特征并进行了验证：单摆的混沌运动与非混沌运动的相图比较体现出非线性相的前提;在改变外力幅度和初始角度的条件下分别比较混沌运动和非混沌运动，以及在改变初始外力，外力频率和阻尼系数是简谐运动到混沌运动转变的过程，可以验证混沌运动对初始条件是极端敏感的。  
3.阻尼单摆在正阻尼条件下演化出奇异吸引子,研究了反映混沌运动特征的奇异吸引子，找到了奇异吸引子的主要特点并且观察到了随着相位的改变，奇异吸引子相应的运动以及改变外力幅度及频率时奇异吸引子的变化，简洁的反映出系统混沌状态的变化。

###致谢（参考文献）
1.百度百科词条：奇异吸引子 单摆 混沌运动等  
2.计算物理 Nicholas J.Giordano, Hisao Nakanishi  
3.李纪强，周斌，丁益民	单摆混沌现象的研究	湖北大学学报（自然科学版）	2013年12月第35卷第4期  
4.杨青勇	单摆的混沌运动	广西民族学院学报（自然科学版）	2003年5月第九卷第2期  
5.李元杰	单摆的规则，随机及混沌运动的研究	大学物理	1998年9月第17卷第9期
