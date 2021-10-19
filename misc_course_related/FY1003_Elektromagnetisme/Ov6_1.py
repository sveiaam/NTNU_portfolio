from mpl_toolkits.mplot3d import Axes3D
from matplotlib.pyplot import figure, show
from matplotlib import cm
from numpy import arange, meshgrid, sqrt

if __name__ == '__main__':
    X = arange(-2, 2, 2 / 100)
    Z = arange(-2, 2, 2 / 100)
    X, Z = meshgrid(X, Z)

    Ve = 1 / sqrt(X ** 2 + (Z - 1 / 2) ** 2) - 1 / sqrt(X ** 2 + (Z + 1 / 2) ** 2)
    Va = Z * (X ** 2 + Z ** 2) ** (-3 / 2)

    fig = figure()
    ax = fig.add_subplot(2, 2, 1, projection='3d')
    surf = ax.plot_surface(X, Z, Ve, cmap=cm.PuOr, vmin=-10, vmax=10)
    ax.set_zlim(-10, 10)
    ax.set_xlabel('x/a')
    ax.set_ylabel('z/a')
    ax.set_zlabel('Ve')

    ax = fig.add_subplot(2, 2, 2, projection='3d')
    surf = ax.plot_surface(X, Z, Va, cmap=cm.PuOr, vmin=-10, vmax=10)
    ax.set_zlim(-10, 10)
    ax.set_xlabel('x/a')
    ax.set_ylabel('z/a')
    ax.set_zlabel('Va')

    ax = fig.add_subplot(2, 2, 3, projection='3d')
    surf = ax.plot_surface(X, Z, 100 * abs((Va - Ve) / Ve), cmap=cm.PuOr, vmin=0, vmax=100)
    ax.set_zlim(0, 100)
    ax.set_xlabel('x/a')
    ax.set_ylabel('z/a')
    ax.set_zlabel('|(Ve-Va)/Ve|*100%')

    show()

#ripoff av utlagt program
