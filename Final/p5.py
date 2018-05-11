import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D
def density(t_end):
    x = np.linspace(-75,75,151)
    y = np.linspace(-75,75,151)
    x,y = np.meshgrid(x,y)
    d = np.zeros((151,151))
    d[75][75]=1
    d1 = deepcopy(d)
    for t in range(t_end):
        for i in range(151):
            for j in range(151):
                if i==0 or i==150 or j==0 or j==150:
                    pass
                else:
                    d[i][j]=0.25*(d1[i+1][j] + d1[i-1][j] + d1[i][j+1] + d1[i][j-1])
        d1=deepcopy(d)
    for i in range(151):
            for j in range(151):
                if i==0 or i==150 or j==0 or j==150:
                    pass
                else:
                    if d[i][j]==0:
                        d[i][j]=0.25*(d1[i+1][j] + d1[i-1][j] + d1[i][j+1] + d1[i][j-1])
    return x,y,d
x,y,z = density(150)[0],density(150)[1],density(150)[2]
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('density')
ax.set_title('Distribution in 2 dimension, t=150')
plt.xlim(-75,75)
plt.ylim(-75,75)
plt.show()