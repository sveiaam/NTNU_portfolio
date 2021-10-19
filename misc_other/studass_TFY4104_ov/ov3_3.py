import numpy as np

#Chosen rather arbitrarily
D = 0.9
L = 1
tol = 1e-5

#Fixed point iteration
def fpi(g, x0, tol):
	'''
	Limited to 200 iterations
	:param g: function; g(x) = x
	:param x0: float; initial value: g(x0) = x1
	:param tol: float; error tolerance
	:return: x: float; fixed point
	:return: S: float; error reduction for final step
	'''
	x = x0; print("x0 =", x)
	counter = 0
	while True:
		counter += 1
		y = g(x)
		z = g(y)
		error1 = abs(x-y)
		error2 = abs(y-z)
		error = (error1 + error2)/2
		S = error2/error1
		print("%-0s %3.0f" % ("iter.", counter) + "   ||  ", "%-4s %4.12f" % ("x =", y) + "   ||  ", "%-4s %4.12f" % ("S =", S))
		if (error < tol) or (counter >= 200):
			break
		x = y
	return x, S

def g1(x):
	return ( 5*D/L - 1 ) / ( 2 * ( 1 + 1/np.sqrt( 1+3*x**2 ) ) )
def g2(x):
	return ( 5*D/L - 1 ) - 2*x / np.sqrt( 1+3*x**2 )
def g3(x):
	return 1/2 * np.sqrt( 1 + 3*x**2 ) * ( 5*D/L - 1 - x )


def main( ):
	x1, s1 = fpi( g1, 0.5, tol )
	x2, s2 = fpi( g2, 0.5, tol )
	#x3, s3 = fpi( g3, 0.5, tol )
	
	print( "alpha 1 : ", np.arctan( x1 ), " = ", np.arctan( x1 ) * 180 / np.pi, " grader " )
	print( "alpha 2 : ", np.arctan( x2 ), " = ", np.arctan( x2 ) * 180 / np.pi, " grader " )
	#print( "alpha 3 : ", np.arctan( x3 ), " = ", np.arctan( x3 ) * 180 / np.pi, " grader " )


if __name__ == "__main__":
	main( )

