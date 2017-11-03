import matplotlib.pyplot as plt
import numpy as np

sigma = 10
b = 8.0 / 3.0
dt = 0.0001


class Lorenz:
	def __init__(self, x, y, z, r):
		self.x = [x]
		self.y = [y]
		self.z = [z]
		self.r = r
		self.t = [0.]
		self.chosen_x = []
		self.chosen_y = []
		self.chosen_z = []

	def update(self):
		current_x = self.x[-1]
		current_y = self.y[-1]
		current_z = self.z[-1]
		# print current_x,current_y,current_z
		a_x = sigma * (current_y - current_x)
		a_y = -current_x * current_z + self.r * current_x - current_y
		a_z = current_x * current_y - b * current_z
		self.next_x = current_x + a_x * dt
		self.next_y = current_y + a_y * dt
		self.next_z = current_z + a_z * dt
		self.next_t = self.t[-1] + dt

	def fire(self):
		while (self.t[-1] <= 500):
			self.update()
			self.x.append(self.next_x)
			self.y.append(self.next_y)
			self.z.append(self.next_z)
			self.t.append(self.next_t)
			if (self.t[-1] >= 30):
				if (abs(self.next_y) < 0.01):
					self.chosen_x.append(self.next_x)
					self.chosen_z.append(self.next_z)
				else:
					pass
			else:
				pass
	
		plt.plot(self.chosen_x, self.chosen_z, ',', label="At x=0,Plot x versus z")



A = Lorenz(1, 0, 0, 25)
A.fire()
plt.legend(loc='upper center')
plt.xlabel('x')
plt.ylabel('z')
plt.show()