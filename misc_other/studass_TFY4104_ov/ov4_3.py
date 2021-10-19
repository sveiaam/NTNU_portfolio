import numpy as np
import matplotlib.pyplot as plt

dt = 0.1
T = np.linspace( 0, 150, 10 )

u = -2.58e3 #m/s
beta = -13.2e3 #kg/s
g = 9.81 #m/s**2
m0 = 3.04e6 #kg

a = np.array( [ u*beta / (m0 + beta*t) - g ] for t in T )
alin = np.array( [ a[0] - u*beta**2/(m0**2) * t ] for t in T )

plt.plot( T, a )
plt.plot( T, alin )
plt.show( )
