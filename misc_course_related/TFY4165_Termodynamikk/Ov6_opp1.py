import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f(x,y):
	return (x+1-2*x*y)/(2*y-y**2-x*y**2)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = y = np.linspace(0.2, 1, 200)
X, Y = np.meshgrid(x, y)
zs = np.array([f(x,y) for x,y in zip(np.ravel(X), np.ravel(Y))])
Z = zs.reshape(X.shape)

ax.plot_surface(X, Y, Z)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('F(x,y)')

plt.show()
