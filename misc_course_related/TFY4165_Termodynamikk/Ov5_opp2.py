from lib import Simpsons_metode as SM
import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mp

def f(x):
	return x/(np.cosh(x))**2

xvalues = np.linspace(0, 5, 500)

plt.plot(xvalues, [SM.simpson(f, 0, i, 500) for i in xvalues], lw=5)
plt.grid()
plt.xlabel('x', size=24)
plt.ylabel('S', size=24)
mp.rcParams.update({'font.size': 24})
plt.show()