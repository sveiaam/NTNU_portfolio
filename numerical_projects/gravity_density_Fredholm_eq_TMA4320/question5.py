## This program plots the solution to question 5 ##

import numpy as np
import pickle
from matplotlib import pyplot as plt
from test_example import analytical_solution
import proj1lib as plib

# Define some things for plotting
font = {'family': 'normal', 'weight': 'bold', 'size': 17}
plt.rc('font', **font)

# Defining constants for the program
a = 0; b = 1
omega = 3 * np.pi; gamma = -2
d1 = 0.025; d2 = 0.25; d3 = 2.5

# Extract the function F
f = pickle.load(open("F.pkl", "rb"))

print("\n##### RUNNING PROGRAM q5 #####\n")

def getRhoHat(xc, xs, xq, w, K, Nq, d, F):
	# Expects collocation, source and quadrature points xc xs xq, wheights w, kernel function K,
		# no. of quadrature panels Nq, constant d and the Force vector in collocation points, F.
	# Returns the rho vector (np.array) for this set of inputs
	A = plib.fredholm_lhs(xc, xs, xq, w, K, Nq, d)
	b = plib.fredholm_rhs(xc, F)
	rhoHat = np.linalg.solve(A,b)
	return rhoHat

def getDiff(N, a, b, d, f):
	# Expects integer N, interval [a,b], constant d, and imported force function f
	# Returns the relative error between the solution rhovec of A*rhovec = b and the rho given by source points
	Ns = Nc = N
	Nq = int(Nc*Nc)
	# Define the set of collocation points and source points
		# Note: The exact syntax of this is due to the way I constructed the chebyshev function
	xc = np.zeros(Nc); xs = np.zeros(Ns)
	XC = plib.chebyshev(plib.rho, a, b, Nc); XS = plib.chebyshev(plib.rho, a, b, Ns)
	# rhovec is gained from the interpolaiton, and represents the actual value of rho
	rhovec = np.zeros(Ns)
	for i in range(Nc):
		xc[i] = XC[(i, 0)]
	for i in range(Ns):
		xs[i] = XS[(i, 0)]
		rhovec[i] = XS[(i, 1)]
	# Generate xq and w from Legendre-Gauss quadrature
	xq, w = np.polynomial.legendre.leggauss(Nq)
	xq = xq * (b-a)/2 + (a+b)/2
	w = w * (b-a)/2
	# Gain the appropriate points given by F
	F = f(xc, d)
	# Calculate rho hat vector and the difference
	rhoHat = getRhoHat(xc, xs, xq, w, plib.K, Nq, d, F)
	return np.linalg.norm((rhoHat - rhovec), np.Inf) / np.linalg.norm(rhovec, np.Inf)
	
def makePlottingVector(xvalues, a, b, d, f):
	# Expects a list of plotting points, xvalues, interval [a,b] constant d and imported force function f
	# Returns a np.array of y-values in the error plot
	print("\nRunning iteration for d = ", d, "\n")
	acc = len(xvalues)
	yvalues = np.zeros(acc)
	for i in range(acc):
		yvalues[i] = getDiff(xvalues[i], a, b, d, f)
		print("It:", i + 1, "of", acc, ":: N =", xvalues[i], ":: Error =", yvalues[i])  ### Only visual
	return yvalues

def plotThreeFunctions(xvalues, yvalues1, yvalues2, yvalues3):
	# Expects a set of x-values and three sets of y-values (np.arrays)
	# Prints the function in the same graph
	plt.semilogy(xvalues, yvalues1, label=r"$d=0.025$", lw=3)
	plt.semilogy(xvalues, yvalues2, label=r"$d=0.25$", lw=3)
	plt.semilogy(xvalues, yvalues3, label=r"$d=2.5$", lw=3)
	
	plt.xlabel(r"$N_{c}$")
	plt.ylabel(r"Relative error")
	
	plt.grid()
	plt.legend(loc='best')
	plt.show()

# Plotting

# Define the x-values in the plot
xvalues = np.arange(5, 30, 1) # Must contain integers. [5,30] is the plotting interval, and the last number is step
# Define the y-values in the plot
err1 = makePlottingVector(xvalues, a, b, d1, f)
err2 = makePlottingVector(xvalues, a, b, d2, f)
err3 = makePlottingVector(xvalues, a, b, d3, f)

plotThreeFunctions(xvalues, err1, err2, err3)
