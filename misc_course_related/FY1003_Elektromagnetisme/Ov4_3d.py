from __future__ import unicode_literals
#from matplotlib.backends.backend_pgf import FigureCanvasPgf
from matplotlib import pyplot as plot
#import matplotlib
from matplotlib import font_manager as fontmg
from matplotlib import rc
import math

def plott(liste_r, liste_rho, liste_Q, liste_E, liste_V):
#    plot.backend_bases.register_backend('pdf', FigureCanvasPgf)
#    matplotlib.use('pgf')
#    plot.rcParams['text.usetex'] = True
#    plot.rcParams['text.latex.unicode'] = True
    plot.plot(liste_r, liste_rho, label = r'$\rho$ / 4$\rho_0$')
    plot.plot(liste_r, liste_Q, label = r'$Q$ / 4$\pi$*$\rho_0$ R^3/3')
    plot.plot(liste_r, liste_E, label = r'$E$ / $\rho_0$R/3$\epsilon_0$')
    plot.plot(liste_r, liste_V, label = r'$V$ / $\rho_0$R^2/3$\epsilon_0$')
    plot.title("Oppg. 3 - d)  :::  Svein Åmdal", fontsize='20')
    plot.xlabel('Avstand fra sentrum (r/R)', fontsize='20')
    plot.ylabel(r'Verdi', fontsize='20')
    ticks_font = fontmg.FontProperties(family='Helvetica', style='normal', size='50', weight='normal', stretch='normal')
        plot.legend()
    plot.grid()
    plot.show()

def main():
    liste_r = []
    liste_rho = []
    liste_Q = []
    liste_E = []
    liste_V = []
    k = 0
    dk = 0.001 #intervall
    while k < 3/2:
        liste_r.append(k)
        if k < 1:
            liste_rho.append(1-k)
            liste_Q.append(4*(k)**3-3*(k)**4)
            liste_E.append(4*(k)-3*(k)**2)
            liste_V.append(2-2*(k)**2+(k)**3)
        else:
            liste_rho.append(0)
            liste_Q.append(0)
            liste_E.append((1/(k))**2)
            liste_V.append(1/(k))

        k += dk

    plott(liste_r, liste_rho, liste_Q, liste_E, liste_V)

main()