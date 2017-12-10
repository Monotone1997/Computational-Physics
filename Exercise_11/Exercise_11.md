# Problem 5.3 电磁场分布的数值求解
## Question
Use the sysmmetry of the capacitor problem (Figure 5.6) to write a program that obtains the results by calculating the potential in only one quadrant of x-y the plane.

## Analysis
在不存在电荷的空间中，电势的分布遵循拉普拉斯方程:  
![](https://camo.githubusercontent.com/0983f05673b5dd953a985b5bdc089f2a9a792c3c/687474703a2f2f692e696d6775722e636f6d2f584536575863582e706e67)  
理论上，只要在一定的边界条件下求解就可以得到静电势的空间分布，但是除了一些特殊的边界条件以外，对于这类问题我们难以得到解析解。所以我们必须使用数值计算的方法，得到电势的数值解。我们使用的方法是Jacobi method:  
![](http://latex.codecogs.com/png.latex?V(i,j)=\frac{1}{4}[V(i+1,j)+V(i-1,j)+V(i,j+1)+V(i,i-1)])  
在计算中，我们总是算完一个点再算另一个点，也就是逐点更新计算结果。该方法主要的改进是在计算某一点的电势时，使用之前的点已经更新（update）后的数据。  
![](https://camo.githubusercontent.com/a218b9c53723a1a7087404a875be86b3872dff31/687474703a2f2f692e696d6775722e636f6d2f684e73754259442e6a7067)  
