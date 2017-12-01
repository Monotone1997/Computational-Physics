# Problem 4.10
## Question
Calculate the precession of perihelion of Mercury, following the approach described in this section.

## Analysis
首先考察一个行星绕太阳的运动的动力学方程。由开普勒定律可知，行星会做圆周运动，或更一般的椭圆运动。由万有引力定律和牛顿第二定律可以写出如下的动力学方程：

![](http://latex.codecogs.com/png.latex?F_G=%5Cfrac%7BG%20M_S%20M_E%7D%7Br%5E2%7D)  
![](http://latex.codecogs.com/png.latex?%5Cfrac%7Bdv_x%7D%7Bdt%7D=-%5Cfrac%7BGM_s%20M_E%20x%7D%7Br%5E3%7D),
![](http://latex.codecogs.com/png.latex?%5Cfrac%7Bdv_y%7D%7Bdt%7D=-%5Cfrac%7BGM_s%20y%7D%7Br%5E3%7D)  

如果我们用天文单位，AU，测量时间，我们发现  

![](http://latex.codecogs.com/png.latex?G%20M_S=v%5E2%20r=4%20%5Cpi%5E2%20%20AU%5E2/yr%5E2)  
利用Euler-Cromer方法，将运动方程转换成差分方程，为构造计算解做准备。  

![](http://latex.codecogs.com/png.latex?v_%7Bx,i+1%7D=v_%7Bx,i%7D-%5Cfrac%7B4%5Cpi%5E2%20x_i%7D%7Br_i%5E3%7D%5CDelta%20t)  
![](http://latex.codecogs.com/png.latex?x_%7Bi+1%7D=x_i%20+v_%7Bx,i+1%7D%5CDelta%20t)  
![](http://latex.codecogs.com/png.latex?v_%7By,i+1%7D=v_%7By,i%7D-%5Cfrac%7B4%5Cpi%5E2%20y_i%7D%7Br_i%5E3%7D%5CDelta%20t)  
![](http://latex.codecogs.com/png.latex?y_%7Bi+1%7D=y_i+v_%7By,i+1%7D%5CDelta%20t)
