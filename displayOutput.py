import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize
from mpl_toolkits.mplot3d import Axes3D


def displayOutput(albedo, height):
    hgt, wid = height.shape
    X,Y = np.meshgrid(np.arange(wid), np.arange(hgt))
    H = np.flipud(np.fliplr(height))
    A = np.flipud(np.fliplr(albedo))

    plt.figure(1)
    ax = plt.axes(projection='3d')

    min = 0.0
    max = 1.0

    scalarMap = cm.ScalarMappable(norm=Normalize(vmin=min, vmax=max), cmap='gray')
    A_colored = scalarMap.to_rgba(A)
    surf = ax.plot_surface(H, X, Y, facecolors=A_colored, linewidth=0)

    plt.title('Estimated surface');
    plt.show()


if __name__ == '__main__':
    displayOutput(np.zeros((50, 50)), np.zeros((50, 50)))
