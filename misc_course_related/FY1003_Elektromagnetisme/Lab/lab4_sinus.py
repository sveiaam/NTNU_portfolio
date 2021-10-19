from matplotlib import pyplot as plt
import numpy as np
import math
from linear_regression import linear_regression

def plott(y, theta, sintheta, justert_y, thetaFit, yreg):
    plt.figure()
    plt.plot(theta, y, lw=3, marker="o", ls="", label=r'y som funksjon av $\theta$')
    plt.plot(thetaFit, yreg, lw=3, label=r'Regresjonskurve')
    plt.grid()
    plt.title(r'y som funksjon av $\theta$', size=20)
    plt.xlabel(r'$\theta$', size=20)
    plt.ylabel('y', size=20)
    plt.legend()
    plt.show()

    plt.figure()
    plt.plot(sintheta, y, lw=3, marker="o", ls="", label=r'y som funksjon av sin($\theta$)')
    plt.plot(sintheta, justert_y, lw=3, label=r'Regresjonskurve')
    plt.grid()
    plt.title(r'y som funksjon av sin($\theta$)', size=20)
    plt.xlabel(r'sin($\theta$)', size=20)
    plt.ylabel('y', size=20)
    plt.legend(loc='upper left')
    plt.show()

def main():
    theta, y = np.loadtxt('sinus.dat',skiprows=0, unpack=True)
    sintheta = np.sin(theta)
    a0, a1 = linear_regression(sintheta, y)
    justert_y = a0+a1*sintheta
    thetaFit = np.linspace(min(theta), max(theta), num=100, endpoint=True, retstep=False)
    yreg = a0+a1*np.sin(thetaFit)
    plott(y, theta, sintheta, justert_y, thetaFit, yreg)

main()