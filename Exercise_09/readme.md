# Problem 3.31
## Question
Study the behavior for other types of tables. One interesting possibility is a square table with a circular interior wall located either in the center, or slightly off-center. Another possibility is an elliptical table.  
  
![](https://github.com/Monotone1997/computationalphysics_N2015301020041/blob/master/Exercise_09/1.png)  

## Analysis
### 桌球模型
Imagine the rebound on the edge of the ball is perfect  
![](https://github.com/Monotone1997/computationalphysics_N2015301020041/blob/master/Exercise_09/2.jpg)  
  
Consider a problem of a ball moving without friction on a perfect billiard table.Between collisions the velocity is constant so we have  
  
![](https://github.com/Monotone1997/computationalphysics_N2015301020041/blob/master/Exercise_09/a.png)  
  
![](https://github.com/Monotone1997/computationalphysics_N2015301020041/blob/master/Exercise_09/b.png)  
  
and  
  
![](https://github.com/Monotone1997/computationalphysics_N2015301020041/blob/master/Exercise_09/c.png)  
  
![](https://github.com/Monotone1997/computationalphysics_N2015301020041/blob/master/Exercise_09/d.png)  


## Codes
### Step1
当球碰到边缘时，我们将这样处理他的碰壁和反弹：
```python
cos=xtry/(xtry**2+ytry**2)**0.5
sin=ytry/(xtry**2+ytry**2)**0.5
verticalx=-(self.vx[i]*cos+self.vy[i]*sin)*cos
verticaly=-(self.vx[i]*cos+self.vy[i]*sin)*sin
#parallelx=self.vx*sin**2-sin*cos*self.vy
#parallely=self.vy*cos**2-self.vx*cos*sin
parallelx=self.vx[i]+verticalx
parallely=self.vy[i]+verticaly
self.vx[i+1]=verticalx+parallelx
self.vy[i+1]=verticaly+parallely
```
[Codes1](https://raw.githubusercontent.com/Monotone1997/computationalphysics_N2015301020041/master/Exercise_09/billiard.py)  
![](https://github.com/Monotone1997/computationalphysics_N2015301020041/blob/master/Exercise_09/QQ%E6%88%AA%E5%9B%BE20171117215815.jpg)  
![](https://github.com/Monotone1997/computationalphysics_N2015301020041/blob/master/Exercise_09/3771733-7f180a30aacecd59.png)
