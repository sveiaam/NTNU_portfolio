import math

r = 0
R = 90  # mm
Q = 900 * 10 ** (-9)  # C
E = 0  # ??
alpha = 8 * Q / (5 * math.pi * R ** 3)
rho_1 = alpha
rho_2 = 2 * alpha * (1 - r / R)
rho_3 = 0
epsilon = 8.85 * 10 ** (-12)
k = 1 / (4 * math.pi * epsilon)

print((E*(r/R))/(k*Q/(R**2)))
