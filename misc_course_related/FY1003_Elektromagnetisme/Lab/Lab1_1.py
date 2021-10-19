serie1 = [0.3, 1.4, 2.2, 3.1, 3.6, 4.3, 4.5, 4.8, 5.1, 5.0]
serie2 = [0.4, 1.3, 2.7, 3.6, 4.5, 5.2, 5.7, 6.1, 6.5, 6.6]
serie3 = [0.4, 1.5, 2.5, 3.6, 4.3, 4.9, 5.5, 5.8, 6.1, 6.4]
serie4 = [0.5, 1.5, 2.7, 3.5, 4.4, 4.9, 5.6, 6.0, 6.5, 6.6]
serie5 = [0.4, 1.7, 2.7, 3.7, 4.5, 4.9, 5.5, 6.0, 6.3, 6.6]
x = [.00444, .0163, .0281, .04, .0519, .0637, .0755, .0874, .0992, .1]

from matplotlib import pyplot as plt
import numpy as np
serie0 = [0.4, 1.48, 2.56, 3.5, 4.26, 4.84, 5.36, 5.74, 6.1, 6.24]

plt.plot(x,serie1, label='serie1')
plt.plot(x,serie2, label='serie2')
plt.plot(x,serie3, label='serie3')
plt.plot(x,serie4, label='serie4')
plt.plot(x,serie5, label='serie5')
plt.plot(x,serie0, label='snitt')


plt.xlabel('Avstand, 1/r^2 (1/cm^2)', fontsize=20)
plt.ylabel('Kraft,F (mN)',fontsize=20)
plt.legend()

#z4 = np.polyfit(x, serie0, 1)
#xx=linspace(0,.1,100)
#plt.plot(xx,z4)

plt.show()