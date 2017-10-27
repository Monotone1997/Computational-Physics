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