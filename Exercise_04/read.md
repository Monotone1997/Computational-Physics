# Problem 1.5

## Question
Consider again a decay problem with two types of nuclei of type A into ones of type B, while nuclei of type B, while nuclei of type B decay into ones of type A. Strictly speaking, this is not a "decay" process,since it is possible for the type B nuclei to turn back into type A nuclei. A better analogy would be a resonance in which a system can tunnel or move back and forth between two states A and B which have equal energies. The corresponding rate equations are <br/>
<img src="http://latex.codecogs.com/gif.latex?\frac{dN_A}{dt}=\frac{N_B}{\tau}-\frac{N_A}{\tau}" alt="" title="" /> <br/>
<img src="http://latex.codecogs.com/gif.latex?\frac{dN_B}{dt}=\frac{N_A}{\tau}-\frac{N_B}{\tau}" alt="" title="" /> <br/>
where for simplicity we have assumed that the two types of decay are characterized by the same time constant,τ. Solve this system of equatiions for the numbers of nuclei, NA=100, NB=0, etc., and take τ=1s. Show that your numercial results are consistent with the idea that the system reaches a steady state in which NA and NB are constant. In such a steady state, the time derivatives dNA/dt and dNB/dt should vanish.

## Analysis
Consider the decay of a number of nuclei:
<img src="http://latex.codecogs.com/gif.latex?\frac{dN}{dt}=-\frac{N}{\tau}" alt="" title="" />  <br/>

And we know the Taylor expansion for:<br/>
  ![](http://latex.codecogs.com/gif.latex?N%28%5CDelta%20t%29%3DN%280%29&plus;%5Cfrac%7BdN%7D%7Bdt%7D%5Ccdot%5CDelta%20t&plus;%5Cfrac%7B1%7D%7B2%7D%5Ccdot%5Cfrac%7Bd%5E2N%7D%7Bdt%5E2%7D&plus;...) <br/>
  
Ignore the higher powers terms: 
 ![](http://latex.codecogs.com/gif.latex?N%28%5CDelta%20t%29%5Capprox%20N%280%29&plus;%5Cfrac%7BdN%7D%7Bdt%7D%5Ccdot%5CDelta%20t) <br/>

So we put dNA and dNB in it:
![](http://latex.codecogs.com/gif.latex?N_A%28t&plus;%5CDelta%20t%29%3DN_A%28t%29&plus;%5Cfrac%7BN_B-N_A%7D%7B%5Ctau%7D%5Ccdot%20%5CDelta%20t) <br/>

![](http://latex.codecogs.com/gif.latex?N_B%28t&plus;%5CDelta%20t%29%3DN_B%28t%29&plus;%5Cfrac%7BN_A-N_B%7D%7B%5Ctau%7D%5Ccdot%20%5CDelta%20t) <br/>

## Codes 
由分析知，N_A和N_B的衰变是相互关联的，由初始值到稳定下来需要一段时间，所以可以使用for循环达到这一目的，以每一次的循环输出粒子数和时间，并用pylab绘出N_A和N_B随时间变化的图像。设置的循环次数是1000，事实上，循环次数已经决定了步幅，需要输入的"the time step'*1000是衰变的总时间（横坐标）。
```python
import numpy as np    
import pylab as pl    
Number_A=[]    
Number_B=[]    
t=[]#建立数组
print('the number of A atoms')    
number_a=float(input())    
Number_A.append(number_a)    
print('the number of B atoms')    
number_b=float(input())    
Number_B.append(number_b)    
print('the time of decay')    
tdecay=float(input())    
print('the time step')    
dt=float(input())#定义初始时刻原子数和步长
t.append(0)    
for i in range(1000):    
    NA=Number_A[i]+((Number_B[i]-Number_A[i])/tdecay)*dt    
    NB=Number_B[i]+((Number_A[i]-Number_B[i])/tdecay)*dt    
    tadd=t[i]+dt    
    Number_A.append(NA)    
    Number_B.append(NB)    
    t.append(tadd)#定义循环
t_max=t[-1]    
pl.plot(t,Number_A,'r')    
pl.plot(t,Number_B,'g')#绘制图像
pl.title('the decay between A and B')    
pl.xlabel('the time of decay')    
pl.ylabel('number of atoms')    
pl.xlim(0.00,t_max)    
pl.ylim(Number_B[0],Number_A[0])    
pl.show()
```

## Result
Parameter:
Number fo Nuclei A is 100
Number of Nuclei B is 0
Time constant is 1s
Steps is 0.004
![result](https://github.com/Monotone1997/computationalphysics_N2015301020041/blob/master/Exercise_04/1.jpg)
