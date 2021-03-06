##problem 2.9

>##摘要
第二章作业主要围绕物体考虑空气阻力的情形下，如何使用euler法来解决相关的物理问题。

>##题目背景
作业第一个层次，主要是要求在考虑风阻以及空气密度随海拔的变化对弹道区县的影响，并且求出在哪个角度下发射能使炮弹飞的最远。  
作业的第二个层次是要求开发一套精确打击目标的程序，所给的目标是与炮弹有高度差，要求目标处于炮弹的轨迹上，并求出能够打击目标的最小发射角。  
作业的第三个层次是要求在上一个层次的基础上考虑炮弹发射时的误差以及风阻变化带来的误差，以求进行更准确的打击。  
>##正文
**level1:**要求考虑风阻以及空气密度变化带来的风阻的变化，采用了绝热过程的近似，选取初速度为500m/s的炮弹，以5°为梯度进行扫描，通过画出不同角度的轨迹，来判断最远距离是由哪个角度产生的。你可以在这里得到我的代码[problem2.9](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter2/problem2.9.py),得到的图像如下图所示![picture](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter2/problem2.9.png)  
**level2:**  
**level3:**
>##结论
经过修正的曲线明显高于未加密度修正的曲线，并且可以得出炮弹发射的最远距离是在发射角为45°时产生的。 

##problem 2.19

>##摘要
棒球飞行轨迹模型

>##题目背景
在原有弹道曲线的基础上，忽略了风阻随空气密度变化的影响，但加入了新的考虑因素，如棒球的表面形状以及击球时产生的自旋对轨迹的影响。  
具体表现为由于表面形状的不规则性，风阻不是一个常数，而是随速度变化的。  
具体关系为：![picture1](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter2/picture1.gif)  
而自旋速度也产生一个浮力，具体关系为：![picture2](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter2/picture2.gif)  
控制vx，vz的情况下观察轨迹的变化,在这里讨论了转速为2000rpm的情况.

>##正文
分别只改变VX和只改变VZ，保证转速不变的情况下棒球的运动轨迹。  
你可以在这里得到我的代码。[problem2.19](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter2/problem2.19.py)
程序得到的两幅图像如下：
![picture3](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter2/picture3.png)  
![picture4](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter2/picture4.png)

