import math
from matplotlib import pyplot as plt
import lib.Simpsons_metode as sp
import numpy as np

#########################################

R = 8.3144621 #Universell gasskonstant
p0 = 1.45E5 #trykk på bakkenivå i Pascal
m = 14E-3 #midlere molar masse i kilogram
Z = 500 #maks høyde for integrasjon i km
g = 1.35 #tilnærmet verdi for tyngdeakselerasjonen i m/s^2
k = 1000 #antall iterasjoner av prosessen
n = 1000 #antall punkter vurdert i Simpsons metode. Partall. Større n gir større nøyaktighet
H = 40E3 #Beregnet i oppg. b - verdien av H for T = 91

#########################################

def T(z):
    return 1/(91.0 - 0.09*z + 3*(math.e)**(-0.1*z))

def p(z):
    return p0*(math.e)**(-(m*g)/R*sp.simpson(T, 0, z, n))

def p2(z):
    return p0 * (math.e) ** (-z/H)

def lagpunkter(k):
    a = np.zeros(k)
    b = np.zeros(k)
    q = Z/k
    r = 0
    for i in range(k):
        a[i] = p(r)/1000
        b[i] = r
        r += q
    return a, b

def lagpunkter2(k):
    a = np.zeros(k)
    q = Z/k
    r = 0
    for i in range(k):
        a[i] = p2(r)/1000
        r += q
    return a

def plott(a, b, c):
    plt.plot(b,a, lw=3, label="Temperatur som T(z)")
    plt.plot(b, c, lw=3, label="Temperatur konstant 91K")
    plt.xlabel("Avstand over bakken i km", size=20)
    plt.ylabel("Trykk i kilopascal", size=20)
    plt.grid()
    plt.legend()
    plt.show()

a, b = lagpunkter(k)
c = lagpunkter2(k)
plott(a, b, c)
