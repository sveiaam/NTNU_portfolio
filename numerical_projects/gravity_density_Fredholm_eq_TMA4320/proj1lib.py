## Project common functions and constants library ##

import numpy as np
import random

# Define constants for the program (will be imported into some programs)
a = 0; b = 1; omega = 3*np.pi; gamma = -2
d = 0.025
Nc = Ns = 40

# Kernel of the integral definition of F(x)
def K(x, y, d):
	# Expects floats x y d
	# Returns the Kernel of (2) in the project description given x y d
	return d * (d ** 2 + (y - x) ** 2) ** (-3 / 2)

# Solves the right hand side of the Fredholm equation set
def fredholm_rhs(xc, F):
	# Expects collocation points xc, F(x) = function for the force in a coll.point
	# Returns the vector F = [F(x_0^c),  ..., F((x_(Ns-1)^c)]
	Nc = xc.shape[0]
	b = np.zeros(Nc)
	for i in range(len(b)):
		b[i] = F[i]
	return b

# Solves the left hand side of the Fredholm equation set
def fredholm_lhs(xc, xs, xq, w, K, Nq, d):
	# Expects collocation points xc, source points xs, quadrature points xq, quadrature weights w (All np.arrays)
	# and K = integral kernel
	# Returns The np matrix A s.t. A*rho = F
	Nc = xc.shape[0]
	Ns = xs.shape[0]
	A = np.zeros((Nc, Ns))
	a = 0
	for i in range(Nc):
		for j in range(Ns):
			a = 0
			for k in range(Nq):
				a += w[k] * K(xc[i], xq[k], d) * lagrangePolyJ(j, xq[k], xs)
			A[(i, j)] = a
	return A

# Lagrange polynomials
def lagrangePolyJ(j, x, xs):
	# Expects the basis poly nr. j, the evaluation point x, the list of interpol. points xs of length >= j
	# Returns the value of the j-th Lagrange polynomial in x
	a = 1
	b = 1
	for m in range(len(xs)):
		if m != j:
			a *= (x - xs[m])
			b *= (xs[j] - xs[m])
	return a / b

# The test function for rho
def rho(x):
	# Expects float x
	# Returns the test value of rho(x) as given on page 4 of the project description
	return np.sin(omega * x) * np.e ** (gamma * x)

# Mapping used (mainly) for Chebyshev
def conformalMapping(x, a, b):
	# Expects a point x E [-1,1] and interval limits a, b
	# Returns w in the mapping from x E [-1,1] to w E [a,b]
	return round(x * (b - a) / 2 + (a + b) / 2, 10)

# Chebyshev interpolation nodes
def chebyshev(f, a, b, n):
	# Expects an integer n = the number of interpolation points (on the interval [-1,1], function f(x) to be
	# interpolated and interval limits a, b
	# Returns the np array [[x0,f(x0)], [x1,f(x1)], ..., [x(n-1),f(x(n-1))]] = The interpolation points for the n-th
	# chebyshev polynomial on the interval [a,b]
	A = np.zeros((n, 2))
	for i in range(n):
		A[(i, 0)] = conformalMapping(np.cos((np.pi / 2 + np.pi * i) / n), a, b)
	for i in range(n):
		A[(i, 1)] = f(A[(i, 0)])
	return A

# Chebyshev interpolation nodes
def chebyshevQ8(a, b, n):
	# Expects an integer n = the number of interpolation points (on the interval [-1,1], function f(x) to be
	# interpolated and interval limits a, b
	# Returns the np array [[x0,f(x0)], [x1,f(x1)], ..., [x(n-1),f(x(n-1))]] = The interpolation points for the n-th
	# chebyshev polynomial on the interval [a,b]
	A = np.zeros(n)
	for i in range(n):
		A[i] = conformalMapping(np.cos((np.pi / 2 + np.pi * i) / n), a, b)
	return A

# Newton-Côtes midpoint quadrature
def midpointNC_x_w(f, a, b, N):
	# Expects a function f(x), interval [a,b] and N number of panels
	# Returns the np array [x0, x1, ..., x(n-1)] and the np array [w0, w1, ..., w(n-1)] for the x-values and weights
	# for a midpoint quadrature of f(x) on N panels.
	x = np.zeros(N)
	w = np.zeros(N)
	h = (b - a) / N
	for i in range(N):
		x[i] = a + h / 2 + i * h
		w[i] = h
	return x, w

# Difference for plotting in quests 3 and 4
def maxDiff(xc, xs, xq, w, K, nq, d, rhovec, F):
	# Expects collocation and source points xc and xs, xvalues and weights, xq and w from some numerical integration
		# method, kernel K, integer nq=len(xq), the vector of rho values and the vector F in collocation points
	# Returns the maximum relative difference between A*rhovec and F for the desired value of nq
	A = fredholm_lhs(xc, xs, xq, w, K, nq, d)
	b = np.dot(A, rhovec)
	diff = np.linalg.norm((F - b), np.Inf) / np.linalg.norm(b, np.Inf)
	return diff

# Nudge the vector b with a perturbation of order delta
def getRandomPerturbation(vecB, delta):
	# Expects vector vecB and error interval delta > 0 (error E [-delta, delta])
	# Returns the vector bTilda with each value randomized to be within b_i +- delta
	Nc = len(vecB)
	bTilda = np.zeros(Nc)
	# Generate random numbers and place them in bTilda

	bTilda = vecB + np.random.uniform(-delta, delta, Nc)
	return bTilda

#New optimilized system of equations
def tikhonovSystem(A,vecB,L):
	"""
	:param A: The matrix A corresponding to the system of equations
	:param vecB: A numpy array of force-measurements
	:param L: Tikhonov regul. parameter lambda (real number)
	:return: Solution to the new system (eq 10) (A numpy array of rho-values)
	"""
	#Variables
	size = A.shape[0]
	At = A.transpose()
	
	#New matrix (Left hand side)
	B = (np.matmul(At,A)+L*np.identity(size))

	#Solve system B*rho = At*vecB and return solution rho
	return np.linalg.solve(B, np.matmul(At,vecB))

#Newton divided differences (calculates corresponding coefficients)
def newton_dd(x_points, y_points, print_coeff):
    """
    Polynomial interpolation: P(x) = c0 + c1(x-x0) + c2(x-x0)(x-x1) + c3(x-x0)(x-x1)(x-x2) + ...
    :param x_points: array of x-datapoints
    :param y_points: array of y-datapoints
    :return: array of coefficients for newtons di.differences inter. polynomial.
    """
    lx = len(x_points)
    ly = len(y_points)
    coeff = np.zeros(lx+1)
    if lx != ly:
        print("The entered lists aren't equally long. Correct this.")
        return 0

    f = np.zeros(shape=(lx, ly))

    for j in range(0, lx):
        f[j][0] = y_points[j]

    for i in range(1, lx):
        for j in range(0, lx - i):
            f[j][i] = (f[j + 1][i - 1] - f[j][i - 1]) / (x_points[j + i] - x_points[j])

    for i in range(0, lx):
        coeff[i] = (f[0][i])

    if print_coeff:
        for i in range(0, lx):
            print("c" + str(i), " = ", round(coeff[i], 10))

    return coeff

#Interpolation with newtons divded differences
def newtonInterPoly(xValues, yValues, x,print_coeff):
    import numpy as np
    """
    :param xValues: array of x-values of the data.
    :param yValues: array of y-values of the data.
    :param x: argument
    :return: interpolation-polynomial evaluated at x.
    """
    #Calculate coefficients
    coeff = newton_dd(xValues,yValues,print_coeff)

    n = len(coeff) - 1  # Degree of polynomial
    pow = np.zeros(n+1)+1
    pow[0] = 1

    for i in range(1,n+1):
        for j in range(0, i):
            pow[i] *= (x - xValues[j])

    return np.dot(pow, coeff)
