import math
import numpy as np
import matplotlib.pyplot as plt

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


def beregninger(fart): #startfart (m/s)
    g = 9.81    #g (ms^-2)
    pos = 0 #vinkel ved start (rad)
    t = 0   #tid etter målestart (s)
    L = 1   #pendellengde (m)
    delta_t = 0.001 #tid mellom hver måling (s)
    counter = 0 #Teller som holder kontroll på perioder
    liste_t = []
    liste_pos = []
    while True:
        print("t =",round(t, 4), "::: vinkel =", round(pos, 5), "::: fart =", round(fart, 5)) ###!!!###
        liste_t.append(t)
        liste_pos.append((180/math.pi)*pos)
        fart = hastighet(fart, pos, delta_t, g)
        previous_pos = pos
        pos = posisjon(pos, fart, delta_t, L, g)
        t += delta_t
        if counter >= 4:
            break
        counter += sjekk_periode(pos, previous_pos)
    print("\nperiode: ",t/2)
    plt.plot(liste_t,liste_pos)
    plt.xlabel('t(s)')
    plt.ylabel('ϴ (grader)')
    plt.show()

beregninger(0.1)

#6.2641787843