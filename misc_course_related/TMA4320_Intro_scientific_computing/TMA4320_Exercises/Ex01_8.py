from scipy.optimize import fsolve
import numpy as np

def f(x):
	return np.sin(x) - x

def main():
	a = fsolve(f, 0.1)
	xa = a[0]
	print("f(x_a) = ", f(xa))

main()
