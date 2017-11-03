# Problem 3.26

## Analysis
### 洛伦兹模型
Lorenz在研究Rayleigh-Benard问题时，将流体力学基本方程组Navier-Stokes方程组化简为简单形式：  
<img src="http://latex.codecogs.com/gif.latex?\frac{dx}{dt}=\sigma(y-x)" alt="" title="" /> <br/>
<img src="http://latex.codecogs.com/gif.latex?\frac{dy}{dt}=-xz+rx-y" alt="" title="" /> <br/>
<img src="http://latex.codecogs.com/gif.latex?\frac{dz}{dt}=xy-bz" alt="" title="" /> <br/>
这个方程组被称为Lorenz方程组，或Lorenz模型。其中x,y,z为变量，其余为常数。

## Codes
### Step1
首先考察Lorenz模型的行为。令sigma=10，b=8/3，改变r的大小，观察z随时间的变化情况（x与y将呈现相似的行为）。
[Codes](https://raw.githubusercontent.com/Monotone1997/computationalphysics_N2015301020041/master/Exercise_08/py1.py)  
![pic1](https://github.com/Monotone1997/computationalphysics_N2015301020041/blob/master/Exercise_08/QQ%E6%88%AA%E5%9B%BE20171103162159.jpg)  
当r=5和10时，图像一开始有一点振荡，随后振幅衰减，z变成一个与时间无关的常数。
当r=25时，图像最终变为混沌状态。

### Step2
接下来考察在相空间中混沌洛伦兹模型z与x的关系。为此我们在x-z平面作图。  
[Codes](https://raw.githubusercontent.com/Monotone1997/computationalphysics_N2015301020041/master/Exercise_08/py2.py)  
![pic2](https://github.com/Monotone1997/computationalphysics_N2015301020041/blob/master/Exercise_08/QQ%E6%88%AA%E5%9B%BE20171103162546.jpg)

### Step3
Phase Space Plot Z Versus x When y=0:   
[Codes](https://raw.githubusercontent.com/Monotone1997/computationalphysics_N2015301020041/master/Exercise_08/py3.py)
![pic3](https://github.com/Monotone1997/computationalphysics_N2015301020041/blob/master/Exercise_08/QQ%E6%88%AA%E5%9B%BE20171103163247.jpg)
