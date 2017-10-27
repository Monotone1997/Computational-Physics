
from pylab import *

dt=0.04
g=9.8
l=9.8
q=0.5
q1=0.5001
FD=1.2
Omega=0.66666666666666

theta=[0.2]
t=[0]
w=[0]
theta1=[0.2]
w1=[0]
delta=[0]

for i in range(100000):

	w_i = w[i] - g*sin(theta[i])*dt/l - q*w[i]*dt + FD*sin(Omega*t[i])*dt
	theta_i = theta[i] + w_i*dt
	t_i = t[i] + dt

	w.append(w_i)
	theta.append(theta_i)
	t.append(t_i)

	w1_i = w1[i] - g * sin(theta1[i]) * dt / l - q1 * w1[i] * dt + FD * sin(Omega * t[i]) * dt
	theta1_i = theta1[i] + w1_i * dt


	w1.append(w1_i)
	theta1.append(theta1_i)
	delta.append(theta1_i-theta_i)

plot(t,delta)

xlim(0,150)
ylim(-0.25,7)
show()