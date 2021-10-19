## This program plots the solution to question 6 ##

import numpy as np
from matplotlib import pyplot as plt
import proj1lib as plib

font = {'family' : 'normal', 'weight' : 'bold', 'size' : 16}
plt.rc('font', **font)

print("\n##### RUNNING PROGRAM q8 #####\n")

def getData(filename):
	"""
	:param filename: name of file as string
	:return: value a, value b, value d, np.array xc, np.array F respectively
	"""
	#Open file
	f = open(filename,'rb')
	npzfile = np.load(f)

	##Print content
	print(npzfile['a'], npzfile['b'], npzfile['d'])
	print(npzfile['xc'])
	print(npzfile['F'])

	return npzfile['a'],npzfile['b'],npzfile['d'],npzfile['xc'],npzfile['F']

def dummyFunction(x):
	return 1

def main():
	#file = "q8_1.npz"
	file = "q8_2.npz"
	#file = "q8_3.npz"

	print("Imported data:\n")

	##Get contruction data
	a,b,d,xc,F = getData(file); Nc = Ns = len(xc); Nq = Nc**2
	#xs = plib.chebyshev(dummyFunction,a,b,Ns)
	xs = plib.chebyshevQ8(a, b, Ns)
	xq,w = np.polynomial.legendre.leggauss(Nq)

	##Tikhonov lamdas

	#L = 5E-4   ## file 1
	L = 5E-6   ## file 2
	#L = 1E-3   ## file 3

	print("\nfile = ", file, " :: Lambda = ", L)
	print("\nCalculating and plotting in progress...\n\n")

	##Map quadrature-interval and weights to [0,2]
	xq = xq*(b-a)/2 + (a+b)/2
	w = w*(b-a)/2

	##Construct matrix A
	A = plib.fredholm_lhs(xc,xs,xq,w,plib.K,Nq,d)

	##Solve Tikhonov-system to get rho-nodes
	rhoNod = plib.tikhonovSystem(A,F,L)

	##Constructing interpolation-polynomial:
	x = np.linspace(a,b,400)
	rhoValues = np.zeros(len(x))
	for i in range(len(x)):
		rhoValues[i] = plib.newtonInterPoly(xs,rhoNod,x[i],False)

	print(rhoValues)
	## Plotting the interpol. polynomial of rho (reconstructed rho)
	plt.plot(x,rhoValues,label=r'$\rho(x), \lambda = $' + str(L), color='g')
	plt.legend(loc='best')
	plt.ylabel(r'$\rho$')
	plt.xlabel(r'$x$')
	plt.grid()
	plt.show()

main()