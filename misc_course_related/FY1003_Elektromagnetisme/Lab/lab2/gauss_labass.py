import numpy
import matplotlib.pyplot as plt 


def getB1(x, R, I, N):
    mu0 = 4.0*numpy.pi*1.0e-7
    return N*mu0*I/(2*R) * (1 + x**2/R**2)**(-1.5) * 1e4


def getB2(x, a, R, I, N):
    return getB1(x-a/2.0, R, I, N) + getB1(x+a/2.0,R,I,N)


def getB3(z, l, R, I, N):
    mu0 = 4.0*numpy.pi*1.0e-7
    return mu0*N*I/(2*l) * (z/numpy.sqrt(z**2 + R**2) + (l-z)/numpy.sqrt((l-z)**2 + R**2)) * 1e4


def measuredData(filename, col):
    f = open(filename, 'r')
    k = []
    for line in f:
        parts = line.split()
        a = parts[col].replace(',', '.')
        k.append(float(a))
    f.close()
    return k


R1 = 0.07
R2 = 0.05
I = 1.0
N1 = 330
N2 = 368
l = 0.396

delta_R1 = 0.001
delta_R2 = 0.001
delta_l = 0.003
delta_x = 0.003
delta_a = 0.002

eps = 1.0e-9
alpha = 0.5

x1 = numpy.linspace(-0.19, 0.19, 100)
x2 = numpy.linspace(-0.1, 0.49, 100)

# simple
sim_dx = (getB1(x1+eps, R1, I, N1) - getB1(x1, R1, I, N1))/eps
sim_dR = (getB1(x1, R1+eps, I, N1) - getB1(x1, R1, I, N1))/eps
sim_x = measuredData('avvik_kort.txt', 0)
sim_data = measuredData('avvik_kort.txt', 1)

# helmholtz a = R/2
h1_dx = (getB2(x1+eps, 0.5*R1, R1, I, N1) - getB2(x1, 0.5*R1, R1, I, N1))/eps
h1_dR = (getB2(x1, 0.5*R1, R1+eps, I, N1) - getB2(x1, 0.5*R1, R1, I, N1))/eps
h1_da = (getB2(x1, 0.5*R1+eps, R1, I, N1) - getB2(x1, 0.5*R1, R1, I, N1))/eps
h1_x = measuredData('avvik_helm.txt', 0)
h1_data = measuredData('avvik_kort.txt', 1)

# helmholtz a = R
h2_dx = (getB2(x1+eps, 1*R1, R1, I, N1) - getB2(x1, 1*R1, R1, I, N1))/eps
h2_dR = (getB2(x1, 1*R1, R1+eps, I, N1) - getB2(x1, 1*R1, R1, I, N1))/eps
h2_da = (getB2(x1, 1*R1+eps, R1, I, N1) - getB2(x1, 1*R1, R1, I, N1))/eps
h2_x = measuredData('avvik_helm.txt', 0)
h2_data = measuredData('avvik_helm.txt', 2)

# helmholtz a = 2R
h3_dx = (getB2(x1+eps, 2*R1, R1, I, N1) - getB2(x1, 2*R1, R1, I, N1))/eps
h3_dR = (getB2(x1, 2*R1, R1+eps, I, N1) - getB2(x1, 2*R1, R1, I, N1))/eps
h3_da = (getB2(x1, 2*R1+eps, R1, I, N1) - getB2(x1, 2*R1, R1, I, N1))/eps
h3_x = measuredData('avvik_helm.txt', 0)
h3_data = measuredData('avvik_helm.txt', 3)

# solenoide
sol_dx = (getB3(x2+eps, l, R2, I, N2) - getB3(x2, l, R2, I, N2))/eps
sol_dR = (getB3(x2, l, R2+eps, I, N2) - getB3(x2, l, R2, I, N2))/eps
sol_dl = (getB3(x2, l+eps, R2, I, N2) - getB3(x2, l, R2, I, N2))/eps
sol_x = measuredData('avvik_sol.txt', 0)
sol_data = measuredData('avvik_sol.txt', 1)
for i in range(0, len(sol_data)):
    sol_data[i] -= 0.155

"""
# simple
plt.figure()
plt.plot(x1, sim_dx, label="dB/dx", lw=3, alpha=alpha)
plt.plot(x1, sim_dR, label="dB/dR", lw=3, alpha=alpha)
plt.title("enkel spole")
plt.legend(loc='best')

a = plt.axes([.2, .2, .2, .2])
plt.plot(x1, (getB1(x1+eps, R1, I, N1) - getB1(x1, R1, I, N1))/eps/getB1(x1, R1, I, N1), lw=3, alpha=alpha)
plt.plot(x1, (getB1(x1, R1+eps, I, N1) - getB1(x1, R1, I, N1))/eps/getB1(x1, R1, I, N1), lw=3, alpha=alpha)
plt.xticks([])
plt.yticks([])
"""

# gauss, simple
plt.figure()
plt.plot(x1, numpy.sqrt((sim_dx*delta_x)**2+(sim_dR*delta_R1)**2), label=r"$\Delta B$", lw=3, alpha=alpha, color='b')
plt.plot(x1, -numpy.sqrt((sim_dx*delta_x)**2+(sim_dR*delta_R1)**2), lw=3, alpha=alpha, color='b')
plt.plot(sim_x, sim_data, lw=3, color="b", marker="o", ls="", label="Avvik")
plt.title("Gauss for enkel spole")
plt.legend(loc='best')
plt.grid()

"""
# helmholtz a = R/2
plt.figure()
plt.plot(x1, h1_dx, label="dB/dx", lw=3, alpha=alpha)
plt.plot(x1, h1_dR, label="dB/dR", lw=3, alpha=alpha)
plt.plot(x1, h1_da, label="dB/da", lw=3, alpha=alpha)
plt.title("a = 0.5R")

plt.legend(loc='best')

a = plt.axes([.2, .2, .2, .2])
plt.plot(x1, (getB2(x1+eps, 0.5*R1, R1, I, N1) - getB2(x1, 0.5*R1, R1, I, N1))/eps/getB2(x1, 0.5*R1, R1, I, N1), label="dB/dx", lw=3, alpha=alpha)
plt.plot(x1, (getB2(x1, 0.5*R1, R1+eps, I, N1) - getB2(x1, 0.5*R1, R1, I, N1))/eps/getB2(x1, 0.5*R1, R1, I, N1), label="dB/dR", lw=3, alpha=alpha)
plt.plot(x1, (getB2(x1, 0.5*R1+eps, R1, I, N1) - getB2(x1, 0.5*R1, R1, I, N1))/eps/getB2(x1, 0.5*R1, R1, I, N1), label="dB/da", lw=3, alpha=alpha)
plt.xticks([])
plt.yticks([])
"""

# gauss, helmholtz a = R/2
plt.figure()
plt.plot(x1, numpy.sqrt((h1_dx*delta_x)**2+(h1_dR*delta_R1)**2+(h1_da*delta_a)**2), label=r"$\Delta B$", lw=3, alpha=alpha, color='b')
plt.plot(x1, -numpy.sqrt((h1_dx*delta_x)**2+(h1_dR*delta_R1)**2+(h1_da*delta_a)**2), lw=3, alpha=alpha, color='b')
plt.plot(h1_x, h1_data, lw=3, color="b", marker="o", ls="", label="Avvik")
plt.title("Gauss for helmholtz a1 = R/2")
plt.legend(loc='best')
plt.grid()

"""
# helmholtz a = R
plt.figure()
plt.plot(x1, h2_dx, label="dB/dx", lw=3, alpha=alpha)
plt.plot(x1, h2_dR, label="dB/dR", lw=3, alpha=alpha)
plt.plot(x1, h2_da, label="dB/da", lw=3, alpha=alpha)
plt.title("a = 1.0R")
plt.legend(loc='best')

a = plt.axes([.2, .2, .2, .2])
plt.plot(x1, (getB2(x1+eps, 1*R1, R1, I, N1) - getB2(x1, 1*R1, R1, I, N1))/eps/getB2(x1, 1*R1, R1, I, N1), label="dB/dx", lw=3, alpha=alpha)
plt.plot(x1, (getB2(x1, 1*R1, R1+eps, I, N1) - getB2(x1, 1*R1, R1, I, N1))/eps/getB2(x1, 1*R1, R1, I, N1), label="dB/dR", lw=3, alpha=alpha)
plt.plot(x1, (getB2(x1, 1*R1+eps, R1, I, N1) - getB2(x1, 1*R1, R1, I, N1))/eps/getB2(x1, 1*R1, R1, I, N1), label="dB/da", lw=3, alpha=alpha)
plt.xticks([])
plt.yticks([])
"""

# gauss, helmholtz a = R
plt.figure()
plt.plot(x1, numpy.sqrt((h2_dx*delta_x)**2+(h2_dR*delta_R1)**2+(h2_da*delta_a)**2), label=r"$\Delta B$", lw=3, alpha=alpha, color='b')
plt.plot(x1, -numpy.sqrt((h2_dx*delta_x)**2+(h2_dR*delta_R1)**2+(h2_da*delta_a)**2), lw=3, alpha=alpha, color='b')
plt.plot(h2_x, h2_data, lw=3, color="b", marker="o", ls="", label="Avvik")
plt.title("Gauss for helmholtz a2 = R")
plt.legend(loc='best')
plt.grid()

"""
# helmholtz a = 2*R
plt.figure()
plt.plot(x1, h3_dx*0.001, label="dB/dx", lw=3, alpha=alpha)
plt.plot(x1, h3_dR*0.0005, label="dB/dR", lw=3, alpha=alpha)
plt.plot(x1, h3_da*0.001, label="dB/da", lw=3, alpha=alpha)
plt.title("a = 2.0R")
plt.legend(loc='best')
plt.grid()

a = plt.axes([.15, .15, .2, .2])
plt.plot(x1, (getB2(x1+eps, 2*R1, R1, I, N1) - getB2(x1, 2*R1, R1, I, N1))/eps/getB2(x1, 2*R1, R1, I, N1), label="dB/dx", lw=3, alpha=alpha)
plt.plot(x1, (getB2(x1, 2*R1, R1+eps, I, N1) - getB2(x1, 2*R1, R1, I, N1))/eps/getB2(x1, 2*R1, R1, I, N1), label="dB/dR", lw=3, alpha=alpha)
plt.plot(x1, (getB2(x1, 2*R1+eps, R1, I, N1) - getB2(x1, 2*R1, R1, I, N1))/eps/getB2(x1, 2*R1, R1, I, N1), label="dB/da", lw=3, alpha=alpha)
plt.xticks([])
plt.yticks([])
"""

# gauss, helmholtz a = 2R
plt.figure()
plt.plot(x1, numpy.sqrt((h3_dx*delta_x)**2+(h3_dR*delta_R1)**2+(h3_da*delta_a)**2), label=r"$\Delta B$", lw=3, alpha=alpha, color='b')
plt.plot(x1, -numpy.sqrt((h3_dx*delta_x)**2+(h3_dR*delta_R1)**2+(h3_da*delta_a)**2), lw=3, alpha=alpha, color='b')
plt.plot(h3_x, h3_data, lw=3, color="b", marker="o", ls="", label="Avvik")
plt.title("Gauss for helmholtz a3 = 2R")
plt.legend(loc='best')
plt.grid()

"""
#solenoid
plt.figure()
plt.plot(x2, sol_dx, label="dB/dz", lw=3, alpha=alpha)
plt.plot(x2, sol_dR, label="dB/dR", lw=3, alpha=alpha)
plt.plot(x2, sol_dl, label="dB/dl", lw=3, alpha=alpha)
plt.legend(loc='best')
plt.title("soilenoide")

a = plt.axes([.4, .15, .2, .2])
plt.plot(x2, (getB3(x2+eps, l, R2, I, N2) - getB3(x2, l, R2, I, N2))/eps/getB3(x2, l, R2, I, N2), label="dB/dz", lw=3, alpha=alpha)
plt.plot(x2, (getB3(x2, l, R2+eps, I, N2) - getB3(x2, l, R2, I, N2))/eps/getB3(x2, l, R2, I, N2), label="dB/dR", lw=3, alpha=alpha)
plt.plot(x2, (getB3(x2, l+eps, R2, I, N2) - getB3(x2, l, R2, I, N2))/eps/getB3(x2, l, R2, I, N2), label="dB/dl", lw=3, alpha=alpha)
plt.xticks([])
plt.yticks([])
"""

# gauss, solenoide
plt.figure()
plt.plot(x2, numpy.sqrt((sol_dx*delta_x)**2+(sol_dR*delta_R2)**2+(sol_dl*delta_l)**2), label=r"$\Delta B$", lw=3, alpha=alpha, color='b')
plt.plot(x2, -numpy.sqrt((sol_dx*delta_x)**2+(sol_dR*delta_R2)**2+(sol_dl*delta_l)**2), lw=3, alpha=alpha, color='b')
plt.plot(sol_x, sol_data, lw=3, color="b", marker="o", ls="", label="Avvik")
plt.title("Gauss for solenoide")
plt.legend(loc='best')
plt.grid()

plt.show(block=True)