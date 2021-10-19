import numpy as np

def solve(A, b):
	'''
	A = square numpy matrix array
	b = numpy vector array

	returns:
	numpy vector array x

	Solution fulfills Ax = b. The solution uses the LU-factorization algorithm with partial pivoting
	'''



def LUfact(A):
	'''
	A = square numpy matrix array
	
	returns:
	numpy matrix array L
	numpy matrix array U
	numpy matrix array P

	Perform PA=LU-decomposition with partial pivoting. L, U, P fulfills PA = LU.
	'''

	# Create a matrix that keeps track of the Gaussian operations on A
	P = np.identity(len(A))
	# Create L and U
	L = U = np.zeros_like(A)

	# For columns (rows of transposed matrix)
	for columns in A.getT():
		# Find maximum entry and indice in column
		V, I = findMaxelementAndIndice(columns[columns::])

			



def findMaxelementAndIndice(x):
	'''
	x = numpy vector array

	returns:
	float V
	int I

	Given the vector x, V is the maximum (absolute) value in the vector, and I is the indice of said max value
	'''
	V = 0
	I = 0
	for i in range(len(x)):
		if abs(x[i]) > V:
			V = abs(x[i])
			I = i

	return V, I

