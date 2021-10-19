import numpy as np
import Ex02_10 as polint

a=10e-4
b=10e4
tol = 10e-10

def conformalMapping(x, a, b):  #returns w in the mapping from x E [-1,1] to w E [a,b]
	return round(x*(b-a)/2 + (a+b)/2, 10)

def conformalMapping2(w, a, b): #returns zeta in the mapping from w E [a,b] to zeta E [1,e]
	return round((np.e-1)*w/2 + (np.e+1)/2, 10)

def f(x):   #returns the function we try to interpolate evaluated at x
	return np.log(x)

def findChebDeg(a, b, n, tol):
	maxError = 1/n * (b-a)**n / 2**(2*n-1) * 1/x**n

def someFunction(x): #returns k such that e^k <= x < e^(k+1).
	e = np.e
	k = 0
	while True:
		if x > e:
			x = x/e; k += 1
		elif x < 1:
			x = x*e; k -= 1
		else:
			break
	return k


def chebyshev(n):   #returns the n interpolation points of chebyshev polynomial no. n (T_n(x))
	A = np.zeros((n,2))
	for i in range(n):
		A[(i,0)] = conformalMapping(np.cos((np.pi/2 + np.pi*i)/n), a, b)
	for i in range(n):
		A[(i,1)] = f(A[(i,0)])
	return A

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

polint.main(chebyshev(7))