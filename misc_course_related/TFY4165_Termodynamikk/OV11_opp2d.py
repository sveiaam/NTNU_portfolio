import numpy as np
from matplotlib import pyplot as plt

h = 1.05*10**(-34)
k_B = 1.38*10**(-23)
omega = 1*10**14


def Z(n, T):
	s = 0
	for i in range(n):
		s += (i+1)*(i+2)/2 * np.e**(-1/(k_B*T) * h*omega*(i+3/2))
	return s

def F(n, T):
	return -k_B*T*np.log(Z(n, T))

def U(n, T):
	s = 0
	for i in range(n):
		s += (i+1)*(i+2)/2 * h*omega*(i+3/2) * np.e**(-1/(k_B*T) * h*omega*(i+3/2))
	return 1/Z(n, T) * s

def S(n):
	return k_B * np.log((n+1)*(n+2)/2)

Tvalues = np.linspace(1, 500, 1000)
Helmholtz_fri = [F(20, T) for T in Tvalues]
Indre_energi = [U(20, T) for T in Tvalues]
Entropi = [S(20) for i in range(len(Tvalues))]

plt.figure()
plt.plot(Tvalues, Helmholtz_fri, label='F')
plt.plot(Tvalues, Indre_energi, label='U')
plt.plot(Tvalues, Entropi, label='S')
plt.legend()
plt.show()