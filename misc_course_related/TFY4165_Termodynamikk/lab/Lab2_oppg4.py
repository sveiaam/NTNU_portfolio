import numpy as np
from matplotlib import pyplot as plt
from lib import read_csv as rd
#import scipy.optimize as opt

a1 = rd.read_csv('Tabell 2.4 Chase.csv')     #Leser inn data som np.array
R = 8.314472    #Universell gasskonstant i kalorier
Theta = 300      #Vil optimere denne
a1[:,1] = a1[:,1]-R

plt.figure()
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.plot(a1[:,0], a1[:,1], marker='o', ls='', lw=3, label='Eksperimentelle data')

plt.xlabel(r'$\textit{T}$ / K', fontsize=18)
plt.ylabel(r'$\textit{C}$ / $cal$ $\cdot$ $mol^{-1}$ $\cdot$ $K^{-1}$', fontsize=18)
plt.grid()
plt.legend(loc='upper left')
plt.title('Plott 4', size=18)
plt.show()
