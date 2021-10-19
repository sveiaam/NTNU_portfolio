import numpy as np
from matplotlib import pyplot as plt

def polIntCoeff(pointarray):  #Expects np.array([[x1,y1], ...[xn,yn]]), returns the interpolation coefficients np.array([f[x1], f[x1,x2], ..., f[x1,x2,...xn]])
	n = len(pointarray)
	c = np.zeros((n,n))     #Creates a nxn matrix to store the temporary coefficients
	coeffs = np.zeros(n)    #Creates a length n array to eventually store the right coefficients
	for i in range(n):      #sets the first row of the matrix equal to the y-values of the interpolation points
		c[(0, i)] = pointarray[(i, 1)]
	for i in range(1,n):    #fills in the rest of an upper-left triangular matrix, where the first column is the top of the "triangle" - i.e. the desired coefficients
		for j in range(n-i):
			c[(i, j)] = (c[(i-1, j+1)] - c[(i-1, j)]) / (pointarray[(i+j, 0)] - pointarray[(j, 0)])
	for i in range(n):
		coeffs[i] = c[(i, 0)]
	return coeffs

def definePlotArea(pointarray): #Expects np.array([[x1,y1], [x2,y2], ...[xn,yn]]), returns the minimum and maximum x-value to be plotted
	n = len(pointarray)
	A = np.zeros(n)
	for i in range(n):
		A[i] = pointarray[(i, 0)]
	sorted_points = np.sort(A)
	minimum, maximum = sorted_points[0], sorted_points[n-1]
	length = maximum - minimum
	rmin = minimum - length/4
	rmax = maximum + length/4
	return rmin, rmax

def pol(x, coeff, pointarray):  #Expects np.array([[x1,y1], [x2,y2], ...[xn,yn]]), returns the interpolating polynomial evaluated at x
	n = len(coeff)
	y = coeff[0]
	t = 1
	for i in range(1,n):
		for j in range(i):
			t *= (x - pointarray[(j,0)])
		y += coeff[i] * t
		t = 1
	return y

def checkForDuplX(pointarray):  #expects np.array([[x1,y1], [x2,y2], ...[xn,yn]]), returns True if xi=xj for some i =! j
	n = len(pointarray)
	A = np.zeros(n)
	for i in range(n):
		A[i] = pointarray[(i,0)]
	l = np.unique(A)
	if len(l) == len(A):
		return False
	else:
		return True

def polIntPlot(pointarray): #Expects np.array([[x1,y1], [x2,y2], ...[xn,yn]]), plots the points and the interpolating polynomial
	coeffs = polIntCoeff(pointarray)
	n = len(coeffs)
	rmin, rmax = definePlotArea(pointarray)
	xvalues = np.linspace(rmin, rmax, acc)
	yvalues = np.zeros(acc)
	for i in range(acc):
		yvalues[i] = pol(xvalues[i], coeffs, pointarray)
	plt.plot(xvalues, yvalues, lw=3, color='r', label="Interpolating polynomial")
	plt.plot(pointarray[:,0], pointarray[:,1], marker='o', ls='', ms=12, color='k', label="Inerpolation points")
	plt.xlabel("x", size=24)
	plt.ylabel("y", size=24)
	plt.grid()
	plt.legend()
	plt.title("Polynomial interpolation with Newton's divided differences method", size=24)
	plt.show()

#Resulution of plotting window
acc = 200

def main(A):
	assert not checkForDuplX(A)
	polIntPlot(A)

A = np.array([[-3,5],[2,7],[0,-1],[4,9]])
main(A)
