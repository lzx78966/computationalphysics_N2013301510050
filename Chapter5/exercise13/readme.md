## problem 5.3

>##摘要
利用Jacobi方法计算了具有两固定势能的金属条的方形势场中电势能的分布情况，并在matplotlib下做出展示。

>##背景
在不存在带电粒子的空间中，电势能分布可由laplace方程得出,laplace方程为：  
![1](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter5/exercise13/1.png)  
如果加上边界条件，理论上我们就可以解出电势V。但是除了一些特殊的边界条件以外，对于这类问题我们难以得到解析解。所以我们必须使用数值计算的方法，得到电势的数值解。

>##正文
利用对称性优化算法，当所求势场存在对称性时，在每一步更新ΔV的过程中，只需计算其中的对称部分，然后根据对称性直接对其他部分赋值即可。  
你可以在这里得到我的[代码](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter5/exercise13/problem5.3.py)。  
处于y轴正负轴两边分别具有大小相同方向相相反的恒定势能，在边界处势能为0的势场得到的结果如下图所示：  
![2](https://github.com/lzx78966/computationalphysics_N2013301510050/blob/master/Chapter5/exercise13/2.png)

>##结论
对于具有两固定势能的金属条,其方形势场中电势能的分布与势场的性质有关。  
对于上述势场可通过只计算x-y平面第一象限得到：在每一步更新V的操作中，首先利用镜面对称得到第二象限的值，然后利用旋转对称得到三、四象限的值。
