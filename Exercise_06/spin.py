import math
from math import *
from pylab import *

t=100000
dt=0.1
g=9.8
s0m=4.1e-4
w=1000*2*3.14/60
b2m=4e-5
delta=5
vd=35
y0=6.5
vx0=70*1000/3600
vx00=95*1000/3600

x=[0]
y=[]
z=[0]
vx=[]
vy=[0]
y.append(y0)
vx.append(vx0)
x1=[0]
y1=[]
vx1=[]
vy1=[0]
y1.append(y0)
vx1.append(vx0)

x2=[0]
y2=[]
vx2=[]
vy2=[0]
y2.append(y0)
vx2.append(vx00)

for i in range (int(t/dt)):
	v=sqrt(vx[i]**2+vy[i]**2)
	b2m=0.0039+0.0058/(1+math.exp(v-vd)/delta)
	v_x=vx[i]-b2m*v*vx[i]*dt
	v_y=vy[i]-g*dt+s0m*w*vx[i]*dt
	vx.append(v_x)
	vy.append(v_y)
	temp_x = x[i] + vx[i] * dt
	temp_y = y[i] + vy[i] * dt
	if x[i] <= 20:
		x.append(temp_x)
		y.append(temp_y)
	else:
		break
plot(x,y,color='g',label="backspin")

for i in range(int(t/dt)):
	v1=sqrt(vx1[i]**2+vy1[i]**2)
	b2m1=0.0039+0.0058/(1+math.exp(v1-vd)/delta)
	v_x1=vx1[i]-b2m1*v1*vx1[i]*dt
	v_y1=vy1[i]-g*dt
	vx1.append(v_x1)
	vy1.append(v_y1)
	temp_x1=x1[i]+vx1[i]*dt
	temp_y1=y1[i]+vy1[i]*dt
	if x1[i] <= 20:
		x1.append(temp_x1)
		y1.append(temp_y1)
	else:
		break
plot(x1,y1,color='r',label="no spin")

for i in range(int(t/dt)):
	v2=sqrt(vx2[i]**2+vy2[i]**2)
	b2m2=0.0039+0.0058/(1+math.exp(v2-vd)/delta)
	v_x2=vx2[i]-b2m2*v2*vx2[i]*dt
	v_y2=vy2[i]-g*dt
	vx2.append(v_x2)
	vy2.append(v_y2)
	temp_x2=x2[i]+vx2[i]*dt
	temp_y2=y2[i]+vy2[i]*dt
	if x2[i] <= 20:
		x2.append(temp_x2)
		y2.append(temp_y2)
	else:
		break
plot(x2,y2,color='b',label="fastball")

grid(True)
title('baseball')
xlabel('x(m)')
ylabel('y(m)')
legend(loc='upper right',frameon=False)
show()