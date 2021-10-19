from matplotlib import pyplot as plt
import matplotlib as mp
import numpy as np
from lib import read_csv as rd


#Noen konstanter
m0 = 6.093 #Aluminiumets masse i gram
t_al = 4.16666667   #tid der al ble lagt til i min
t_kok = 5.1666667   #tid der al kokte i min
Theta = 318.5
n = 0.233   #antall mol aluminium
R = 8.314472   #universell gasskonstant
T0 = 295 #romtemp i kelvin
Tf = 77 #kokepkt for N2 i kelvin
L = 2.0*10**5   #Fordampingsvarme for aluminium

data = rd.read_csv('lab2_tabell.csv')

xdata = np.linspace(0, 500, 1000)

def Epsilon(y):
	return y/(np.e**y-1)

def plottfunksjon(theta, delta_m, T0):
	return L*delta_m - 3*n*R*(T0*Epsilon(theta/T0)-Tf*Epsilon(theta/Tf))

dm = 4.61 * 10**(-3)   #fordampet masse sfa aluminium
dm_min = 4.48 * 10**(-3)   #usikkerhet
dm_max = 4.74 * 10**(-3)

T0_max = 296    #usikkerhet i romtemp i Kelvin
T0_min = 294

#Plotter figuren med måledataene
plt.figure()

plt.plot(xdata, [plottfunksjon(i, dm, T0) for i in xdata], lw=4, color='k', label=r'Løsning for $\Theta$')
plt.plot(xdata, [plottfunksjon(i, dm_max, T0_max) for i in xdata], ls='dashed', lw=4, color='r', label='Løsningsintervall medregnet usikkerhet')
plt.plot(xdata, [plottfunksjon(i, dm_min, T0_min) for i in xdata], ls='dashed', lw=4, color='r')
plt.plot([0, 500], [0,0], lw=3, label='Nullinje')
#Spesifikasjoner for plottet
plt.xlabel(r'$\Theta_{E}$', size=28)
plt.ylabel('Løsning', size=28)
plt.legend(fontsize=28, loc=2)
plt.grid()
mp.rcParams.update({'font.size': 24})
plt.show()
#(1) = Løsningen for Theta
#(2) = Medregnet usikkerhet
#(3) = Null
