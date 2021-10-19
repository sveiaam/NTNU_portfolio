import numpy as np
from matplotlib import pyplot as plt
from lib import read_csv as rd
#import scipy.optimize as opt

a1 = rd.read_csv('Tabell 2.2 Giauque Meads.csv')     #Leser inn data som np.array
R = 8.314472*0.239005736    #Universell gasskonstant i kalorier
Theta = 295     #Vil optimere denne

def funk(T, t):
	return 3*R*(t/T)**2*(np.e**(t/T))/((np.e**(t/T)-1)**2)  #Funksjon som etterlignes

xdata = np.linspace(a1[0,0], a1[-1,0], 500)
y = np.zeros(len(xdata))
ydata = np.array([funk(i, Theta) for i in xdata]) * 4.184 #mult for å få SI-enheter
#y_noise = a1[:,1]
#ydata = y2 + y_noise

#popt, pcov = opt.curve_fit(funk, xdata, ydata, bounds=(1000, 1500))

plt.figure()
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.plot(a1[:,0], a1[:,1]*4.184, marker='o', ls='', lw=3, label='Eksperimentelle data') #mult for SI
plt.plot(xdata, ydata, lw=3, label=r'Teoretisk resultat for $\Theta$ = 300 K')

#plt.plot(opt.curve_fit(lambda t: funk(T, t), xdata, ydata))
#plt.plot(xdata, funk(xdata, *popt), label='2')

plt.xlabel(r'$\textit{T}$ / K', fontsize=18)
plt.ylabel(r'$\textit{C}$ / $cal$ $\cdot$ $mol^{-1}$ $\cdot$ $K^{-1}$', fontsize=18)
plt.grid()
plt.legend(loc='upper left')
plt.title('Plott 2', size=18)
plt.show()
