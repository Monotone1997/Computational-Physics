# Problem 5.3 电磁场分布的数值求解
## Question
Use the sysmmetry of the capacitor problem (Figure 5.6) to write a program that obtains the results by calculating the potential in only one quadrant of x-y the plane.

## Analysis
在不存在电荷的空间中，电势的分布遵循拉普拉斯方程:  
![](https://camo.githubusercontent.com/0983f05673b5dd953a985b5bdc089f2a9a792c3c/687474703a2f2f692e696d6775722e636f6d2f584536575863582e706e67)  
理论上，只要在一定的边界条件下求解就可以得到静电势的空间分布，但是除了一些特殊的边界条件以外，对于这类问题我们难以得到解析解。所以我们必须使用数值计算的方法，得到电势的数值解。我们使用的方法是relaxation method，这种方法可以用来数值求解以拉普拉斯方程为代表的一类所谓的“椭圆偏微分方程”。
