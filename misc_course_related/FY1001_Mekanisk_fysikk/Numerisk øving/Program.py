import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager as fontmg

def hastighet(fart0, vinkel0, delta_t, g):
    fart_etter = fart0 + aks(g, vinkel0) * delta_t
    return fart_etter

def aks(g, theta):
    return -g * math.sin(theta)

def posisjon(pos0, fart, delta_t, L, g):
    pos_etter = pos0 + fart/L * delta_t
    return pos_etter

def sjekk_periode(vinkel, previous):
    if vinkel >= 4*math.pi:
        return 4
    elif vinkel > 0 and previous < 0:
        return 1
    elif vinkel < 0 and previous > 0:
        return 1
    else: return 0

def mekanisk_energi(v, g, vinkel,L):
    K = (1/2)*v**2 + g*abs(L*(1-math.cos(vinkel)))
    return K

def beregninger(fart_0): #startfart (m/s)
    g = 9.81    #g (ms^-2)
    pos = 0 #vinkel ved start (rad)
    t = 0   #tid etter målestart (s)
    L = 1   #pendellengde (m)
    delta_t = 0.001 #tid mellom hver måling (s)
    counter = 0 #Teller som holder kontroll på perioder
    fart = fart_0
    liste_t = []
    liste_pos = []
    liste_mekeng = []
    mek_energi = 1/2*fart**2
    while True:
        print("t =",round(t, 4), "::: vinkel =", round(pos, 5), "::: fart =", round(fart, 5)) ###!!!###
        liste_t.append(t)
        liste_pos.append((180/math.pi)*pos)
        liste_mekeng.append(mek_energi)
        fart = hastighet(fart, pos, delta_t, g)
        previous_pos = pos
        pos = posisjon(pos, fart, delta_t, L, g)
        mek_energi = mekanisk_energi(fart, g, pos, L)
        t += delta_t
        if counter >= 4:
            break
        counter += sjekk_periode(pos, previous_pos)
    print("\nperiode: ",t/2)
    plt.plot(liste_t,liste_pos)
    ticks_font = fontmg.FontProperties(family='Helvetica', style='normal', size='30', weight='normal', stretch='normal')
    plt.title("Startfart = 9 m/s", fontsize='20')
    plt.xlabel('t(s)', fontsize='20')
    plt.ylabel(r'$\theta$ (grader)', fontsize='20')
    plt.grid()
    plt.show()
    plt.plot(liste_t, liste_mekeng)
    plt.title("Startfart = 6.2641787843 m/s", fontsize='20')
    plt.xlabel('t(s)', fontsize='20')
    plt.ylabel('K/m (Joule/kilogram)', fontsize='20')
    plt.grid()
    plt.ylim(-2,30)
    plt.show()

beregninger(9)

#6.2641787843