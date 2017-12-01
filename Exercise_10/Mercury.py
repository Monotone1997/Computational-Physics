import pylab as pl
import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import animation

class circle():
    def __init__(self,x0=1,y0=0,t0=0,vx0=0,vy0=2*math.pi,dt0=0.001,total_time=10):
        self.x=[x0]
        self.y=[y0]
        self.vx=[vx0]
        self.vy=[vy0]
        self.R=x0**2+y0**2
        self.t=[t0]
        self.dt=dt0
        self.T=total_time
    def run(self):
        for i in range(int(self.T/self.dt)):
            vx=self.vx[-1]-(4*math.pi**2*self.x[-1]/self.R**2)*self.dt
            vy=self.vy[-1]-(4*math.pi**2*self.y[-1]/self.R**2)*self.dt
            self.vx.append(vx)
            self.vy.append(vy)
            self.x.append(self.vx[-1] * self.dt + self.x[-1])
            self.y.append(self.vy[-1] * self.dt + self.y[-1])
    def show(self):
        pl.plot(self.x, self.y, '-', label='tra')
        pl.xlabel('x(AU)')
        pl.ylabel('y(AU)')
        pl.title('Earth orbiting the Sun')
        pl.xlim(-1.2,1.2)
        pl.ylim(-1.2,1.2)
        pl.axis('equal')
        pl.show()
a=circle()
a.run()
a.show()