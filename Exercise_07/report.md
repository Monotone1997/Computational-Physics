# Problem 3.14

## Question
Repeat the previous problem, but give the two pendulums slightly different damping factors. How does the value of Lyapunov exponent compare with that found in Figure 3.7?

## Abstract
本文先对课本上已有的实验结论进行了模拟分析，简要讨论了单摆阻尼、外界驱动力、非线性现象等因素的影响，并以此为基础，解答了相关问题。
## Analysis
对于有外力驱动下的有阻尼单摆,满足的方程如下，

<img src="http://latex.codecogs.com/gif.latex?\frac{d^2\theta}{dt^2}=-\frac{g}{l}sin\theta-q\frac{d\theta}{dt}+F_Dsin(\Omega_Dt)" alt="" title="" /> <br/>

<img src="http://latex.codecogs.com/gif.latex?\frac{d\theta}{dt}=\omega" alt="" title="" /> <br/>

用Eular-Cromer Method能容易的得到theta-t和w-t的图像，接着考虑的是这个系统方程的稳定性，改变一点点初始角度或其他参数，绘制出Delta theta 随时间变化的曲线:
<img src="http://latex.codecogs.com/gif.latex?\Delta%20t\approx%20e^{\lambda%20t}" alt="" title="" /> <br/>

## Codes
### step 1
首先是对课本中给定的图像进行的模拟，参数和变量如下
q=1/2, l=g=9.8, Omega=2/3, dt=0.04, theta(0)=0.2, w(0)=0
```python
import math
from math import *
from pylab import *
dt=0.04
g=9.8
l=9.8
q=0.5
FD=1.2
Omega=0.66666666666666
theta=[0.2]
t=[0]
w=[0]
for i in range(100000):
	w_i = w[i] - g*sin(theta[i])*dt/l - q*w[i]*dt + FD*sin(Omega*t[i])*dt
	theta_i = theta[i] + w_i*dt
	t_i = t[i] + dt
	if theta_i>3.14:
		theta_i -= 6.28
	elif theta_i<-3.14:
		theta_i += 6.28
	else:
		theta_i = theta_i
	w.append(w_i)
	theta.append(theta_i)
	t.append(t_i)
# plot phase-space graph
plot(theta,w)
xlim(-3.3,3.3)
# plot(t,theta) xlim(0,60)
show()
```
运行的结果如图：
![]()
![]()
### step 2
接下来考虑两个相同的摆，改变其中一个的耗散因子q，计算出Delta theta随时间变化的曲线
[Codes]()


