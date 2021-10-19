serie1 = [2.8, 1.2, 0.5, 0.2]
serie2 = [2.4, 1.1, 0.5, 0.2]
serie3 = [2.4, 1.1, 0.4, 0.1]
serie4 = [2.4, 1.2, 0.5, 0.1]
serie5 = [2.4, 1.1, 0.5, 0.2]

serie0 = [2.48, 1.14, 0.48, 0.16]

Q = [1, 1/2, 1/4, 1/8]

from matplotlib import pyplot as plt
plt.plot(Q, serie1, label='serie 1')
plt.plot(Q, serie2, label='serie 2')
plt.plot(Q, serie3, label='serie 3')
plt.plot(Q, serie4, label='serie 4')
plt.plot(Q, serie5, label='serie 5')
plt.plot(Q, serie0, label='gj.snitt')
plt.xlabel('Q')
plt.ylabel('F')
#plt.legend()
plt.show()