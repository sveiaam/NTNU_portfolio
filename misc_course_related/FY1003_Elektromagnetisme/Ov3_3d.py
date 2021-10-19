from matplotlib import pyplot as plot
from matplotlib import font_manager as fontmg
import math

def plott(liste_r, liste_E, liste_rhoalpha):
    plot.plot(liste_r, liste_E)
    plot.plot(liste_r, liste_rhoalpha)
    plot.title("Oppg. 3 - d)", fontsize='20')
    plot.xlabel('radius (r/R)', fontsize='20')
    plot.ylabel(r'Blå = E/kQ/R^2  :::  Grønnn = $\rho$/$\alpha$', fontsize='20')
    ticks_font = fontmg.FontProperties(family='Helvetica', style='normal', size='50', weight='normal', stretch='normal')
    plot.grid()
    plot.show()

def main():
    liste_r = []
    liste_E = []
    liste_rhoalpha = []
    r=0
    R = 90 #mm
    Q = 900*10**(-9) #C
    E = 0 #??
    alpha = 8*Q/(5*math.pi*R**3)
    epsilon = 8.85*10**(-12)
    k = 1/(4*math.pi*epsilon)
    rho = alpha
    while r < 200: #200mm
        liste_r.append(r/R)
        liste_E.append(E*(R**2)/(k*Q))
        liste_rhoalpha.append(rho/alpha)
        r += 0.01 #INTERVALL (dr)
        if r < R/2:
            E = alpha/(3*epsilon)*r
            rho = alpha
        elif R/2 < r < R:
            E = alpha/(epsilon*r**2)*((2/3*r**3)-(r**4/(2*R))-(R**3/96))
            rho = 2*alpha*(1-r/R)
        else:
            E = k*Q/r**2
            rho = 0
    plott(liste_r, liste_E, liste_rhoalpha)

main()