import matplotlib.pyplot as plt
import math


def trac(vyy):
	x = [1]
	y = [0]
	vx = [0]
	vy = [vyy]
	t = [0]
	dt = 0.002

	while t[-1] <= 1.8:
		r2 = (x[-1]) ** 2 + (y[-1]) ** 2
		r = math.sqrt(r2)
		ox = -4 * math.pi * math.pi * x[-1] / (r ** 3)
		oy = -4 * math.pi * math.pi * y[-1] / (r ** 3)
		vx.append(vx[-1] + ox * dt)
		vy.append(vy[-1] + oy * dt)
		x.append(x[-1] + vx[-1] * dt)
		y.append(y[-1] + vy[-1] * dt)
		t.append(t[-1] + dt)

	return x, y


fig = plt.figure(figsize=[8, 8])
x1 = trac(2 * math.pi)[0]
y1 = trac(2 * math.pi)[1]
x2 = trac(2.2 * math.pi)[0]
y2 = trac(2.2 * math.pi)[1]
x3 = trac(2.4 * math.pi)[0]
y3 = trac(2.4 * math.pi)[1]
x4 = trac(2.6 * math.pi)[0]
y4 = trac(2.6 * math.pi)[1]
plt.plot(x1, y1, label='v=v0')
plt.plot(x2, y2, label='v=1.1v0')
plt.plot(x3, y3, label='v=1.2v0')
plt.plot(x4, y4, label='v=1.3v0')
plt.scatter([0], [0], s=100, color='red')
plt.legend(loc='upper right',frameon=False)
plt.xlim(-4, 1.5)
plt.ylim(-2.5, 2.5)
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')
plt.title('trajectory for different initial velocity')
plt.grid(True,linestyle = "-.")

plt.show()


