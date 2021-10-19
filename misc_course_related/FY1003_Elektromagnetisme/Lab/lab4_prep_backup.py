#Scriptet gjør det labheftet ber om og er laget av Svein Åmdal
import numpy as np
from matplotlib import pyplot as plt
import math

def plott(xakse, yakse, yakse2, yakse3):
    plt.figure()
    plt.plot(xakse, yakse, lw=3, marker="o", ls="", label='Måleverdier')
    plt.plot(xakse, yakse2, lw=3, label='Regresjonskurve')
    plt.grid()
    plt.title('Måleverdier og regresjonskurve', size=20)
    plt.xlabel('x', size=20)
    plt.ylabel('y', size=20)
    plt.legend()
    plt.show()

    plt.plot(xakse, yakse3, lw=3, label='avvik fra y')
    plt.grid()
    plt.title('Avvik fra regresjonskurve', size=20)
    plt.xlabel('x', size=20)
    plt.ylabel('y', size=20)
    plt.show()

def main():
    A = np.loadtxt('data.dat',skiprows=0)
    liste_x = []
    malte_y = []
    delta_y = []
    justert_y = []
    N = len(A)
    Sx, Sy, Sxx, Sxy = 0, 0, 0, 0

    for i in range(len(A)):
        liste_x.append(A[i][0])
        malte_y.append(A[i][1])
        Sx += A[i][0]
        Sy += A[i][1]
        Sxx += (A[i][0])**2
        Sxy += A[i][0] * A[i][1]

    Delta = N * Sxx-(Sx)**2
    a0 = (Sy*Sxx-Sx*Sxy)/(Delta)
    a1 = (N*Sxy-Sx*Sy)/(Delta)

    for i in range(len(A)):
        justert_y.append(malte_y[i]-(malte_y[i]-(a0+a1*liste_x[i])))
        delta_y.append(malte_y[i]-(a0+a1*liste_x[i]))

    S = 0

    for i in range(len(A)):
        S += (malte_y[i]-a0-a1*liste_x[i])**2

    delta_a0 = math.sqrt((1)/(N-2)*(S*Sxx)/(Delta))
    delta_a1 = math.sqrt((N)/(N-2)*(S)/(Delta))

    plott(liste_x, malte_y, justert_y, delta_y)
    print('a0:',a0)
    print('a1:', a1)
    print('D_a0:', delta_a0)
    print('D_a1:', delta_a1)

main()
