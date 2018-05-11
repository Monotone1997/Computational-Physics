# Random Systems 随机系统
`赵宇飞` `2015301020041`
## Abstract 摘要
- 物理学中有一些系统，是确定性的系统，它们由某些准确的数学模型加上边界条件所描述，比如谐振子，它们有唯一确定解，而有另一些物理系统，它们不能用准确的表达式描述，其中，随机性扮演着非常重要的角色，这类系统一般称为**随机系统**。这类系统，一个明显的特征就是拥有非常多的自由度，或者与粒子数相关，或者与自旋相关。  
- 一个代表性的随机问题是扩散问题，扩散是一种常见的随机过程。在扩散现象中，每个粒子的运动都可看作独立的随机行走。因此，随机行走与布朗运动类似，是布朗运动的理想数学状态。尽管在模拟随机行走的过程中，不考虑粒子服从的真实动力学规律，但当模拟的时间足够长、模拟粒子数足够多后，就可以准确的描述真实系统的统计学规律。  
## Random Walk and Diffusion process 随机行走与扩散过程
### Analysis 分析
#### 一维随机游走
首先应该讨论随机系统中最简单的一维情况。从起点开始，第一步等可能的向左或向右。我们能将位置描述为关于时间的函数。  
另一个更有趣和更丰富的量是n步之后的位移**平方的平均值**。平均x^2与t成比即与步数n成比例,即：  
![](http://latex.codecogs.com/png.latex?\%3Cx^2%3E=2Dt)  
![](http://i2.bvimg.com/643282/5881f4caae48ae37.png)  
#### 二维扩散
对于更普遍的二维情况，如分子的自由扩散，数目和位移的函数关系满足高斯分布。  
![](http://latex.codecogs.com/png.latex?\rho(i,n+1)=\rho(i,n)+\frac%20{D%20\Delta%20t}{\left(\Delta%20x\right)^2}\left[\rho(i+1,n)+\rho(i-1,n)-2\rho(i,n)\right])  
![Markdown](http://i1.bvimg.com/643282/6e63fedb248cc14c.png)  
随着时间的增大，密度曲线的峰值下降，范围增大，总面积保持不变。 
![Markdown](https://raw.githubusercontent.com/Monotone1997/Computational-Physics/master/Final/Figure_4.png)  
![Markdown](https://raw.githubusercontent.com/Monotone1997/Computational-Physics/master/Final/Figure_3.png)  
![Markdown](https://raw.githubusercontent.com/Monotone1997/Computational-Physics/master/Final/Figure_5.png)  
#### 二维扩散熵
熵的统计定义：![](http://latex.codecogs.com/png.latex?S=%20-\sum_{i}^n%20P_i\ln%20{P_i})
### Codes 代码实现
相比于其他语言，使用python完成随机数的生成十分简单，仅需要两行代码。当然也可以通过种子生成质量更高的随机数。
```
import random
r=random.uniform(0,1)
```
由于是要求x^2的平均值，所以要再写一个循环每次输出平均值。
```
for i in range(m):
    x2=x2+Random_walk()[1]
x2=x2/(m+1)
```
[**All the Codes**](https://github.com/Monotone1997/Computational-Physics/tree/master/Final)  
