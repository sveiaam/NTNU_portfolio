from matplotlib import pyplot as plt

Tc = [11.0, 10.8, 8.8, 7.1, 5.4, 3.9, 2.7, 1.5]
Th = [10.7, 13.5, 16.2, 18.6, 20.8, 23.0, 25.1, 26.7]
t = [0, 2, 4, 6, 8, 10, 12, 14]

plt.plot(t, Tc, label='Tc', lw=5, marker='o')
plt.plot(t, Th, label='Th', lw=5, marker='o')
plt.legend()
plt.xlabel('Tid i minutter', size=20)
plt.ylabel('Temeratur i celcius', size=20)
plt.grid()
plt.show()





