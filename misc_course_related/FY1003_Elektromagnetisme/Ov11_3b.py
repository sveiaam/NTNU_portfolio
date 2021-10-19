from matplotlib import pyplot as plt

d_zeta = 0.001
d_alpha = 0.05
BB, z = [], []
zeta = -1
alpha = 1.9

while alpha < 2.1:
    while zeta <= 1:
        BB.append(((1/(alpha**2+(zeta+1)**2))**(3/2)+(1/(alpha**2+(zeta-1)**2))**(3/2))/(2*(1/(alpha**2+1))**(3/2)))
        z.append(zeta)
        zeta += d_zeta
    plt.figure()
    plt.plot(z, BB, lw=3)
    plt.grid()
    plt.xlabel(r'$\zeta$', size=20)
    plt.ylabel(r'$\frac{B}{B_0}$', size=20)
    plt.title(r'Oppg. 3b - Svein Åmdal ::: $\alpha$ = ' + str(alpha.__round__(2)), size=20)
    plt.show()

    zeta = -1
    alpha += d_alpha
    BB = []
    z = []
