import numpy as np
from matplotlib import pyplot as plt
from lib import read_csv as rd
import matplotlib as mp

a1 = rd.read_csv('Tabell 2.3 Buyco Davis.csv')
R = 8.314472
Theta = 318.5
Theta_max = 335.1
Theta_min = 301.9

def funk(Theta, T):
	return 3*R*(Theta/T)**2 * (np.e**(Theta/T))/(np.e**(Theta/T)-1)**2

temps = np.linspace(1, 900, 1800)

plt.figure()
#plt.rc('text', usetex=True)
#plt.rc('font', family='serif')
plt.plot(a1[:,0], a1[:,1]*113.1, marker='o', ls='', color='k', lw=16, label='Eksperimentelle data, Buyco og Davis')
plt.plot(temps, [funk(Theta, i) for i in temps], lw=7, color='r', label='Teoretiske verdier')
#plt.plot(temps, [funk(Theta_max, i) for i in temps], lw=3, ls='dashed', label=r'Maksimal $\Theta_{E}$')
plt.plot(temps, [funk(Theta_min, i) for i in temps], lw=7, color='b', ls='dashed', label=r'Teoretiske verdier for minimal $\Theta_{E}$ innenfor usikkerhet')
plt.xlabel(r'$T$ / K', fontsize=28)
plt.ylabel(r'$c_{V m}$ / J mol$^{-1}$ K$^{-1}$', fontsize=28)
plt.grid()
plt.legend(loc=4, fontsize=26)
mp.rcParams.update({'font.size': 24})
plt.show()
