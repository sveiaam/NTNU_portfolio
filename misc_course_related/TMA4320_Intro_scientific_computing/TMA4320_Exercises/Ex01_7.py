import numpy as np

def fpi(g, x0, tol): #returns x,S: g(x)=x to the order of tol for initial x0
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

#The exercise spesific functions
def g1(x):
	return np.e**(x-2)+x**3
def g2(x):
	return (np.e**(x-2))/(1-x**2)
def g3(x):
	return np.log(x-x**3)+2
def g4(x):
	return (x-np.e**(x-2))**(1/3)
def g5(x):
	return (x-np.e**(x-2))/(x**2)
def g6(x):
	return 1-(np.e**(x-2))/(x**2+x)
def g7(x):
	return 1/x - (np.e**(x-2))/(x**2)
def g8(x):
	return -1-(np.e**(x-2))/(x**2-x)
def f(x):
	return np.e**(x-2)+x**3-x

def function_iteration(function, x0, tol, functionname_str):
	print("\n:::::::::::::::::::::::::")
	print("\nRunning function", functionname_str, ":")
	r, S = fpi(function, x0, tol)
	print("\nThe fixed point is", r)
	print("f(x) =", round(f(r), 10))
	return round(r, 6)

def main():
	tol = 10e-12
	a = function_iteration(g1, 0, tol, "g1(x)")
	#function_iteration(g2, 0, tol, "g2(x)")
	#function_iteration(g3, 0.2, tol, "g3(x)")
	b = function_iteration(g4, 1, tol, "g4(x)")
	#function_iteration(g5, 2, tol, "g5(x)")
	#function_iteration(g6, -2, tol, "g6(x)")
	#function_iteration(g7, 1, tol, "g7(x)")
	c = function_iteration(g8, 2, tol, "g8(x)")

	print(a, b, c)


main()
