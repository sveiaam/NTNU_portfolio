import numpy as np

tol = 0.00000001

def f(x):   #This is the polynomial for calculating det(A)
	return -15-x*(12*x-90)+6*(11*x-80) - 2*(-12-x*(84-9*x)+6*(77-8*x)) + 3*(4*(12*x-90)-5*(84-9*x)+6*(70-x*x)) - x*(4*(11*x-80)-5*(77-8*x)+x*(70-x*x))

def bisection(a,b,function, tol, const):   #Returns x: functionx(x) = const. [a,b] is the interval, tol is the accuracy
	while (b-a)/2 > tol:
		c = (a+b)/2
		if function(c) == 0:
			return c
		if (function(c)-const)*(function(a)-const) < 0:
			b = c
		else:
			a = c
	return (a+b)/2

def main():
	root1 = round(bisection(0,1000, f, tol, 1000), 6)
	print("x =", root1)
	A = np.array(([1,2,3,root1],
	              [4,5,root1,6],
				  [7,root1,8,9],
	              [root1,10,11,12]))
	a = np.linalg.det(A)
	print("Determinant =", a)

	root2 = round(bisection(-1000, 0, f, tol, 1000), 6)
	print("x =", root2)
	B = np.array(([1,2,3,root2],
	              [4,5,root2,6],
				  [7,root2,8,9],
	              [root2,10,11,12]))
	b = np.linalg.det(B)
	print("Determinant =", b)


main()
