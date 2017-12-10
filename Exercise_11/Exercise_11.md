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


## Codes
首先建立平板处为±1，其他地方为0的网格
```
grid = []
for i in range(201):    
    row_i = []
    for j in range(201):
        if i == 0 or i == 200 or j == 0 or j == 200:
            voltage = 0
        elif 70<=i<=130 and j == 70:
            voltage = 1
        elif 70<=i<=130 and j == 130:
            voltage = -1
        else:
            voltage = 0
        row_i.append(voltage)
grid.append(row_i)
```
使用迭代语句令非边界上的点的电势相等于其周围最近的四个点的电势的平均值。
```
def update_V(grid):

    delta_V = 0

    for i in range(201):    
        for j in range(201):
            if i == 0 or i == 200 or j == 0 or j == 200:
                pass
            elif 70<=i<=130 and j == 70:
                pass
            elif 70<=i<=130 and j == 130:
                pass
            else:
                voltage_new = (grid[i+1][j]+grid[i-1][j]+grid[i][j+1]+grid[i][j-1])/4
                voltage_old = grid[i][j]
                delta_V += abs(voltage_new - voltage_old)
                grid[i][j] = voltage_new

return grid, delta_V
```
在计算某一点的电势时，使用之前的点已经更新（update）后的数据。最终扩散得到全局电势。
```
def Laplace_calculate(grid):

    epsilon = 10**(-5)*200**2
    grid_init = grid
    delta_V = 0
    N_iter = 0

    while delta_V >= epsilon or N_iter <= 10:
        grid_impr, delta_V = update_V(grid_init)
        grid_new, delta_V = update_V(grid_impr)
        grid_init = grid_new
        N_iter += 1

return grid_new
```

本单元的习题与前几章已经能熟练使用的欧拉法有本质性不同，由于能力有限，本章在书写时较多的参考了吴雨桥学姐的代码。
[Codes](https://github.com/Monotone1997/computationalphysics_N2015301020041/blob/master/Exercise_11/potential.py)  
![](https://github.com/Monotone1997/computationalphysics_N2015301020041/blob/master/Exercise_11/2.jpg)  
![](https://github.com/Monotone1997/computationalphysics_N2015301020041/blob/master/Exercise_11/1.jpg)
