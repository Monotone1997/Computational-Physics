import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D

sigma=10
b=8.0/3.0
dt=0.001
x0=1.
y0=0.
z0=0.

class Lorenz:
	def __init__(self,r):
		self.x=[x0]
		self.y=[y0]
		self.z=[z0]
		self.r=r
		self.t=[0.]

	def update(self):
		current_x=self.x[-1]
		current_y=self.y[-1]
		current_z=self.z[-1]
		a_x=sigma*(current_y-current_x)
		a_y=-current_x*current_z+self.r*current_x-current_y
		a_z=current_x*current_y-b*current_z
		self.next_x=current_x+a_x*dt
		self.next_y=current_y+a_y*dt
		self.next_z=current_z+a_z*dt
		self.next_t=self.t[-1]+dt

	def fire(self):
		while (self.t[-1]<=50):
			self.update()
			self.x.append(self.next_x)
			self.y.append(self.next_y)
			self.z.append(self.next_z)
			self.t.append(self.next_t)
			
		plt.plot(self.t,self.z,label='r='+str(self.r))

A=Lorenz(25)
A.fire()
A=Lorenz(10)
A.fire()
A=Lorenz(5)
A.fire()
plt.legend(loc='best')
plt.xlim(0,50)
plt.xlabel('t')
plt.ylabel('z')
plt.show()