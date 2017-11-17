import pylab as pl
import numpy as np
import math


class tabel:
    def __init__(self, x0=0.2, y0=0, vx0=-0.2, vy0=-0.5, dtstep=0.001, total_time=100):
        self.x = [x0]
        self.y = [y0]
        self.vx = [vx0]
        self.vy = [vy0]
        self.time = total_time
        self.t = [0]
        self.dt = dtstep
        self.xbound=[-1]
        self.y1bound=[0]
        self.y2bound=[0]


    def run(self):
        for i in range(int(self.time / self.dt)):
            self.x.append(self.x[i]+self.vx[i]*self.dt)
            self.y.append(self.y[i] + self.vy[i] * self.dt)
            self.vx.append(self.vx[i])
            self.vy.append(self.vy[i])
            if (self.x[i+1]**2+self.y[i+1]**2>1):
                xtry=(self.x[i]+self.x[i+1])/2
                ytry=(self.y[i]+self.y[i+1])/2
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


                if (xtry**2+ytry**2>1):
                    self.x[i+1]=xtry
                    self.y[i+1]=ytry
                    continue
                else:
                    self.x[i]=xtry
                    self.x[i]=ytry
                    continue

    def bound(self):
        self.xbound= [-1]
        self.y1bound = [0]
        self.y2bound = [0]
        dx = 0.001
        for i in range (2000):
            self.xbound.append(self.xbound[i]+dx)
            self.y1bound.append(abs(1-self.xbound[i+1]**2)**0.5)
            self.y2bound.append(-abs(1-self.xbound[i+1]**2)**0.5)
    def show(self):
        pl.plot(self.x,self.y,'.',label='tra')
        pl.plot(self.xbound,self.y1bound,'--',label='bound')
        pl.plot(self.xbound,self.y2bound,'--',label='bound')
        pl.xlabel(u'x')
        pl.ylabel(u'y')
a=tabel()
a.run()
a.bound()
a.show()
pl.show()