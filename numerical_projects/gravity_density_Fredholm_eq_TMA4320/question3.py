## This program plots the solution to question 3 ##

import numpy as np
import pickle
from matplotlib import pyplot as plt
from test_example import analytical_solution    ## Imports the test data
import proj1lib as plib     ## Imports the project common functions

# Define some things for plotting
font = {'family': 'normal', 'weight': 'bold', 'size': 17}
plt.rc('font', **font)

# Import constants from project library
a = plib.a; b = plib.b; omega = plib.omega; gamma = plib.gamma
d = plib.d; Nc = plib.Nc;Ns = plib.Ns

print("\n##### RUNNING PROGRAM q3 #####\n")

def makePlottingVector(nq, Nc, Ns, d, a, b):
	# Expects a integer filled np.array nq, constants Nc and Ns, constant d, interval limits a and b
	# Returns a np array of the error between F and A * rhovec, as described by previous functions
	acc = len(nq)
	# Define the set of collocation points and source points
		# Note: The exact syntax of this is due to the way I constructed the chebyshev function
	plotvec = np.zeros(acc)
	xc = np.zeros(Nc); xs = np.zeros(Ns)
	XC = plib.chebyshev(plib.rho, a, b, Nc); XS = plib.chebyshev(plib.rho, a, b, Ns)
	rhovec = np.zeros(Ns)
	for i in range(Nc):
		xc[i] = XC[(i, 0)]
	for i in range(Ns):
		xs[i] = XS[(i, 0)]
		rhovec[i] = XS[(i, 1)]
	# Extract the force F in each collocation point as a np array
	f = pickle.load(open("F.pkl", "rb"))
	F = f(xc, d)
	# Calculate b and compare with F. Insert difference in plotvec
	for i in range(acc):
		xq, w = plib.midpointNC_x_w(plib.rho, 0, 1, nq[i])
		plotvec[i] = plib.maxDiff(xc, xs, xq, w, plib.K, nq[i], d, rhovec, F)
		print("It:", i + 1, "of", acc, ":: Nq =", nq[i], ":: Error =", plotvec[i])  ### Only visual
	return plotvec

# Plotting
def plotFunction(xlist, ylist):
	plt.plot(xlist, ylist, lw=3)
	plt.grid()
	plt.title(r"Relative error as a function of $N_{s}$ with Midpoint Newton-Cotes")
	plt.xlabel(r"$N_{s}$")
	plt.ylabel(r"Relative error")
	plt.show()


nq = np.arange(5,250+1,40)  # must consist of integers, choose which values you want
plotvec = makePlottingVector(nq, Nc, Ns, d, a, b)

plotFunction(nq, plotvec)