from math import *
from pylab import *

x=[0]
y=[0]
x1=[0]
y1=[0]
vx=[100]
vy=[300]
vx1=[100]
vy1=[300]
g=9.8
b2m=4e-5
a=6.5e-3
t=100000
dt=0.1
T_0=288

for i in range(int(t/dt)):
	c=sqrt(vx1[i]**2+vy1[i]**2)
	p=(2.71828)**(-(y1[i]*0.00001))
	f=b2m*c**2*p*(1-a*y1[i]/T_0)**2.5
	theta_x=vx1[i]/c
	theta_y=vy1[i]/c
	v_x1=vx1[i]-f*theta_x*dt
	v_y1=vy1[i]-f*theta_y*dt-g*dt
	vx1.append(v_x1)
	vy1.append(v_y1)
	temp_x1=x1[i]+vx1[i]*dt
	temp_y1=y1[i]+vy1[i]*dt
	if y1[i]>=0:
		x1.append(temp_x1)
		y1.append(temp_y1)
	else:
		break
plot(x1,y1,color='g',label="Air drag with altitude")

for i in range(int(t/dt)):
	v_x=vx[i]
	v_y=vy[i]-g*dt
	vx.append(v_x)
	vy.append(v_y)
	temp_x=x[i]+vx[i]*dt
	temp_y=y[i]+vy[i]*dt
	if y[i]>=0:
		x.append(temp_x)
		y.append(temp_y)
	else:
		break
plot(x,y,color='b',label="No air drag")

grid(True)
title('Cannon shell trajectory')
xlabel('x(m)')
ylabel('y(m)')
xlim(0,6300)
ylim(0,5000)
legend(loc='upper right',frameon=False)
show()