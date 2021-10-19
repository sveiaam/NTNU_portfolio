## This program plots the solution to question 6 ##

import numpy as np
import pickle
from matplotlib import pyplot as plt
from test_example import analytical_solution
import proj1lib as plib

# Define some things for plotting
font = {'family': 'normal', 'weight': 'bold', 'size': 17}
plt.rc('font', **font)

# Defining constants for the program
a = plib.a; b = plib.b
omega = plib.omega; gamma = plib.gamma
d1 = 0.025; d2 = 0.25; d3 = 2.5
delta = 0.001
Nc = Ns =30
Nq = Nc * Nc

# Extract the function F
f = pickle.load(open("F.pkl", "rb"))

print("\n##### RUNNING PROGRAM q6 #####\n")

def getValues(a, b, d, f, xc, xs):
	# Expects interval [a,b], constant d and imported force function f
	# Returns rhoHat, bVec; vectors that solve the equation A*rhoHat = b
	# Generate xq and w from Legendre-Gauss quadrature
	xq, w = np.polynomial.legendre.leggauss(Nq)
	xq = xq * (b - a) / 2 + (a + b) / 2
	w = w * (b - a) / 2
	# Gain the appropriate points given by F
	F = f(xc, d)
	# Calculate rho hat vector and bVec vector
	A = plib.fredholm_lhs(xc, xs, xq, w, plib.K, Nq, d)
	bVec = plib.fredholm_rhs(xc, F)
	rhoHat = np.linalg.solve(A, bVec)
	print("Getting values for d = ", d)
	return rhoHat, bVec


# Define the set of collocation points and source points
# Note: The exact syntax of this is due to the way I constructed the chebyshev function
xc = np.zeros(Nc); xs = np.zeros(Ns)
XC = plib.chebyshev(plib.rho, a, b, Nc); XS = plib.chebyshev(plib.rho, a, b, Ns)
for i in range(Nc):
	xc[i] = XC[(i, 0)]
for i in range(Ns):
	xs[i] = XS[(i, 0)]

# Generate all lists for plotting
rhoHat_d1, bVec_d1 = getValues(a, b, d1, f, xc, xs)
rhoHat_d2, bVec_d2 = getValues(a, b, d2, f, xc, xs)
rhoHat_d3, bVec_d3 = getValues(a, b, d3, f, xc, xs)
rhoHat_d1_pert = plib.getRandomPerturbation(rhoHat_d1, delta)
rhoHat_d2_pert = plib.getRandomPerturbation(rhoHat_d2, delta)
rhoHat_d3_pert = plib.getRandomPerturbation(rhoHat_d3, delta)
bVec_d1_pert = plib.getRandomPerturbation(bVec_d1, delta)
bVec_d2_pert = plib.getRandomPerturbation(bVec_d2, delta)
bVec_d3_pert = plib.getRandomPerturbation(bVec_d3, delta)

# Plot appropriate plots with appropriate colors
def twoPlots(xvalues, rho1, rho1_p, rho2, rho2_p, rho3, rho3_p, b1, b1_p, b2, b2_p, b3, b3_p):
	# Plot of b and b~
	plt.subplot(1,2,1)
	plt.plot(xvalues, b1, label=r'$b_{d1}$', lw=3, color="purple")
	plt.plot(xvalues, b2, label=r'$b_{d2}$', lw=3, color="royalblue")
	plt.plot(xvalues, b3, label=r'$b_{d3}$', lw=3, color="lime")
	plt.plot(xvalues, b1_p, label=r'$\tilde{b}_{d1}$', lw=3, linestyle="--", color="yellow")
	plt.plot(xvalues, b2_p, label=r'$\tilde{b}_{d2}$', lw=3, linestyle="--", color="navy")
	plt.plot(xvalues, b3_p, label=r'$\tilde{b}_{d3}$', lw=3, linestyle="--", color="darkgreen")
	plt.xlabel(r"$x$")
	plt.ylabel(r"$F$")
	plt.grid()
	plt.legend()
	
	# Prepare analytical rho for plotting
	actualRho = np.zeros(len(xvalues))
	for i in range(len(xvalues)):
		actualRho[i] = plib.rho(xvalues[i])
	# Plot of rho and rho~
	plt.subplot(1,2,2)
	plt.plot(xvalues, actualRho, label=r"$Analytical$ $\rho$", lw=3, color="black")
	plt.plot(xvalues, rho1, label=r"$\rho_{d1}$", lw=3, color="purple")
	plt.plot(xvalues, rho2, label=r"$\rho_{d2}$", lw=3, color="royalblue")
	plt.plot(xvalues, rho3, label=r"$\rho_{d3}$", lw=3, color="lime")
	plt.plot(xvalues, rho1_p, label=r"$\tilde{\rho}_{d1}$", lw=3, linestyle="--", color="yellow")
	plt.plot(xvalues, rho2_p, label=r"$\tilde{\rho}_{d2}$", lw=3, linestyle="--", color="navy")
	plt.plot(xvalues, rho3_p, label=r"$\tilde{\rho}_{d3}$", lw=3, linestyle="--", color="darkgreen")
	plt.xlabel(r"$x$")
	plt.ylabel(r"$\rho (x)$")
	plt.grid()
	plt.legend(loc='best')
	plt.show()

twoPlots(xc, rhoHat_d1, rhoHat_d1_pert, rhoHat_d2, rhoHat_d2_pert, rhoHat_d3, rhoHat_d3_pert, bVec_d1, bVec_d1_pert, bVec_d2, bVec_d2_pert, bVec_d3, bVec_d3_pert)
