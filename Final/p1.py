from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
import random

N=100
accuracy=1e-10
class Fields:
	def __init__(self,step):
		self.v=[]
		self.Entropy=[]
		self.step=step
		self.old_v=[]
		for i in range(N):
			self.v.append([])
			self.old_v.append([])

		#print len(self.old_v)

		for i in range(N):
			for j in range(N):
				self.v[i].append(0)
				self.old_v[i].append(0)

		for i in range(N//4,3*N//4):
			for j in range(N//4,3*N//4):
				self.v[i][j]=1

	def update(self):
		s=0
		global temp_Entrpy
		temp_Entropy=0
		self.Delta_v=0.
		for i in range(N):
			self.v[i][0]=0
			self.v[i][N-1]=0

		for j in range(N):
			self.v[0][j]=0
			self.v[N-1][j]=0

		for i in range(N):
			for j in range(N):
				self.old_v[i][j]=self.v[i][j]


		for i in range(1,N-1):
			for j in range(1,N-1):
				self.v[i][j]=(self.old_v[i+1][j]+self.old_v[i-1][j]+self.old_v[i][j+1]+self.old_v[i][j-1])/4.
				s+=self.v[i][j]

		for i in range(N):
			for j in range(N):
				if (self.v[i][j]!=0):
					temp_Entropy+=-(self.v[i][j]/s)*np.log(self.v[i][j]/s)

		self.Entropy.append(temp_Entropy)

	def fire(self):
		counter=0
		for i in range(self.step):
			self.update()
			counter+=1
			i+=1

		plt.plot(np.linspace(1,self.step,self.step),self.Entropy,linewidth=2)
		return self.v

	def draw(self):
		fig = plt.figure()
		ax = fig.gca(projection='3d')
		x=np.linspace(-1,1,N)
		y=np.linspace(-1,1,N)
		x, y = np.meshgrid(x, y)
		surf = ax.plot_surface(x, y, self.fire(), rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
		ax.set_zlim(-1.01, 1.01)

		ax.zaxis.set_major_locator(LinearLocator(10))
		ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
		plt.xlabel("X")
		plt.ylabel("Y")
		fig.colorbar(surf, shrink=0.5, aspect=5)

Super=Fields(1000)
Super.fire()
plt.xlabel("step")
plt.ylabel("Entropy of the system")
plt.title("Entropy of the two dimension system vary over 1000steps(time)")
plt.show()
