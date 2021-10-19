
import numpy as np
import scipy
from pylab import *

# Bruk LaTeX
rc('text',usetex=True)

# Eksperimentelle data for phi og S/g i enheter hhv radianer og gram.
phi = [0.00001, 1.57080, 3.14159, 4.71239, 6.28319, 7.85398, 9.42478, 10.99557, 12.56637]
S = [185.0, 240.0, 300.0, 440.0, 600.0, 800.0, 1000.0, 1100.0, 1400.0]
mu = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
y = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
imax = 9
mumiddel = 0.0
musum = 0.0
# Regner ut mu-verdier:
for i in range(1, imax):
    y[i] = np.log(S[i]/S[0])
#   mu[i] = np.log(S[i]/S[0])/phi[i]
    mu[i] = y[i]/phi[i]
    musum = musum + mu[i]

# Middelverdi av mu:
mumiddel = musum/(imax-1)
# Standardavvik og standardfeil i mu:
kvadratavvik = 0.0
for i in range(1, imax):
    kvadratavvik = kvadratavvik + (mu[i]-mumiddel)**2

deltamu = np.sqrt(kvadratavvik/(imax-2))
deltamumiddel = deltamu/np.sqrt(imax-1)

for i in range(1, imax):
    y[i] = np.log(S[i]/S[0])


# Visualiserer resultatene:
print("mumiddel = ",mumiddel)
print("deltamu = ",deltamu)
print("deltamumiddel = ",deltamumiddel)

plt.scatter(phi,y,label='$\ln(S/S0)$')
plt.hold(True)
phi = np.asarray(phi)
midtlinje = mumiddel*phi
lavlinje = (mumiddel-deltamu)*phi
hoylinje = (mumiddel+deltamu)*phi
plt.plot(phi,midtlinje,label='$\overline{\mu}\,\phi$',color='b')
plt.plot(phi,hoylinje,label='($\overline{\mu}+\Delta\mu)\,\phi$',color='g')
plt.plot(phi,lavlinje,label='($\overline{\mu}-\Delta\mu)\,\phi$',color='r')
plt.title('{\O}ving 3, Oppgave 1')
plt.xlabel('$\phi$ (rad)')
plt.legend(loc='upper left')
plt.axis([0,14,0,2.5])
plt.hold(False)
savefig('pythonfigur.eps')
show()
