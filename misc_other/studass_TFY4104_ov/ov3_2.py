import numpy as np
import matplotlib.pyplot as plt

pi = np.pi

measurements = np.array( [ [0, 185],
						   [pi/2, 240],
						   [pi, 300],
						   [3*pi/2, 440],
						   [2*pi, 600],
						   [5*pi/2, 800],
						   [3*pi, 1000],
						   [7*pi/2, 1100],
						   [4*pi, 1400] ] )

# Smax(theta) = S(0)exp(mu*theta)
# => mu(theta) = 1/theta*ln( Smax(theta) / Smax(0) )

mu = np.zeros( len(measurements) )
for i in range( 1, len(measurements) ):
	mu[i] = 1/measurements[i][0] * np.log( measurements[i][1] / measurements[0][1] )

avg_mu = np.average(mu[1:]) #disregard the case theta = 0

def deltamu( arr ):
	S = 0
	for i in range( len(arr) ):
		S += ( arr[i] - avg_mu )**2
	return np.sqrt( 1/(len(arr)-1) * S )

delta_mu = deltamu( mu[1:] )

std_error = delta_mu / np.sqrt( len(mu[1:]) )

print("Gjennomsnitt: ", avg_mu)
print("Standardavvik: ", delta_mu)
print("Standardfeil: ", std_error)
print()
print("mu = ", avg_mu, " p/m ", std_error)

xvalues = np.arange( 0, 13, 0.1 )

plt.plot( measurements[:,0], np.log( measurements[:,1] / measurements[0][1] ), marker='o', lw=0, label=r'$ln(S/S_{0})$' )
plt.plot( xvalues, avg_mu * xvalues, label=r'$\bar{\mu}\varphi$' )
plt.plot( xvalues, (avg_mu + delta_mu) * xvalues, label=r'$(\bar{\mu}+\Delta\mu)\varphi$' )
plt.plot( xvalues, (avg_mu - delta_mu) * xvalues, label=r'$(\bar{\mu}-\Delta\mu)\varphi$' )
plt.grid( )
plt.xlabel( r'$\varphi$ (rad)' )
plt.legend( )
plt.show( )
