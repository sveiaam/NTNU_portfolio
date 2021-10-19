#Scriptet gjør det labheftet ber om og er laget av Svein Åmdal
import numpy as np
from matplotlib import pyplot as plt
from linear_regression import linear_regression

def plott(xakse, yakse, yakse2, yakse3):    #Plotter funksjonene som spesifisert i labheftet
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
    x, y = np.loadtxt('data.dat',skiprows=0, unpack=True)

    a0, a1 = linear_regression(x, y)

    justert_y = np.array(a0+a1*x)
    delta_y = np.array(y - justert_y)

    plott(x, y, justert_y, delta_y)

main()