## This program plots the solution to question 7 ##

import numpy as np
import pickle
from matplotlib import pyplot as plt
from test_example import analytical_solution
import proj1lib as plib

# Defining some things for plotting:
font = {'family': 'normal', 'size': 17}	#'weight': 'bold', 
plt.rc('font', **font)

# Defining constants for the program
a = 0; b = 1
omega = 3 * np.pi; gamma = -2
d1 = 0.025; d2 = 0.25; d3 = 2.5

# Extract the function F
f = pickle.load(open("F.pkl", "rb"))

print("\n##### RUNNING PROGRAM q7 #####\n")

def getRhoHat(xc, xs, xq, w, K, Nq, d, F):
	# Expects collocation, source and quadrature points xc xs xq, wheights w, kernel function K,
		# no. of quadrature panels Nq, constant d and the Force vector in collocation points, F.
	# Returns the rho vector (np.array) for this set of inputs
	A = plib.fredholm_lhs(xc, xs, xq, w, K, Nq, d)
	b = plib.fredholm_rhs(xc, F)
	rhoHat = np.linalg.solve(A,b)
	return rhoHat

def getDiffQ7(N, a, b, d, f, lambdaList, lambdaIndeks, A, vecBTilde, rhovec):
	# Expects integer N, interval [a,b], constant d, and imported force function f
	# Returns the maximum error between the solution rhovec of A*rhovec = b and the rho given by source points
	Ns = Nc = N
	rhoHatTilde = np.zeros(Nc)
	rhoHatTilde = plib.tikhonovSystem(A,vecBTilde,lambdaList[lambdaIndeks])	
	return np.linalg.norm((rhovec - rhoHatTilde), np.Inf) / np.linalg.norm(rhovec, np.Inf)


def makePlottingVectorQ7(xvalues, a, b, d, f, N, delta):
	# Expects a list of plotting points, xvalues, interval [a,b] of x, constant d, imported force function f and number of collocation- and source points N.
	# Returns a np.array of y-values in the error plot.
	print("\nRunning iteration for d = ", d, "\n")
	
	Ns = Nc = N
	Nq = int(Nc*Nc)
	# Define the set of collocation points and source points
    # Note: The exact syntax of this is due to the way the chebyshev function is constructed
	xc = np.zeros(Nc); xs = np.zeros(Ns)
	XC = plib.chebyshev(plib.rho, a, b, Nc); XS = plib.chebyshev(plib.rho, a, b, Ns)
	# rhovec is gained from the interpolation, and represents the actual values of rho
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
	vecB = plib.fredholm_rhs(xc, F)
	
	# Calculate rho-hat vector (with random errors) and the difference
	vecBTilde = plib.getRandomPerturbation(vecB, delta)
	
	A = plib.fredholm_lhs(xc, xs, xq, w, plib.K, Nq, d)
	yvalues = np.zeros(len(xvalues))
	for i in range(len(xvalues)):
		yvalues[i] = getDiffQ7(N, a, b, d, f, xvalues, i, A, vecBTilde, rhovec) 	#delta = 0.001
	return yvalues

### Plotting
# Define the x-values (lambdaList) for the plot
lambdaList = np.geomspace(1e-14, 10, 100)
# Define the y-values in the plot
rhoDiffListD2 = makePlottingVectorQ7(lambdaList, a, b, d2, f, 30, 1e-3)	# d2 = 0.25, Nc=Ns=N=30
rhoDiffListD3 = makePlottingVectorQ7(lambdaList, a, b, d3, f, 30, 1e-3)

plotD2, = plt.loglog(lambdaList,rhoDiffListD2, lw=3)
plotD3, = plt.loglog(lambdaList,rhoDiffListD3, lw=3)
plt.legend([plotD2, plotD3],[r'$d=0.25$', r'$d=2.5$'])
plt.grid()
plt.xlabel(r'$\lambda$')
plt.ylabel(r'$\max_j |\rho(x_j^s) - \hat{\mathbf{\rho}}_j |$')
plt.suptitle('')
plt.show()


### Results/comments
# The resulting graphs indicate that the maximum difference between rho and rhoHatTilde is smallest for d2=0.25 at lambda=10^(-7) and smallest for d3=2.5 at lambda between 10^(-5) and 10^(-4), e.g. 5.5*10^(-5) (average).
# A good choice for lambda could be for example 5*10^(-6)? (average of the logarithms)