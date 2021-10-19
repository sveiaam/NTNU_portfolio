import numpy as np

n = 100


def jacobi_iteration( A, b, x = None, N = 25 ):
	"""
	
	:param A: np.array([n x n]) - Left hand side matrix
	:param b: np.array([1 x n]) - Right hand side vector
	:param x: np.array([1 x n]) - Initial guess vector
	:param N: Int - Number of iterations
	:return: np.array([1 x n]) - Solution vector
	"""
	
	D = np.diag( A )
	LU = A - np.diagflat( D )
	if x is None:
		x = np.zeros( ( len( b ), 1 ) )
	
	for i in  range( N ):
		x = ( b - np.dot( LU, x ) ) / D
	
	return np.array([ [ x[ i , 0 ] ] for i in range( len( b ) ) ] )



def gauss_seidel_iteration( A, b, x = None, N = 25 ):
	"""
	
	:param A: np.array([n x n]) - Left hand side matrix
	:param b: np.array([1 x n]) - Right hand side vector
	:param x: np.array([1 x n]) - Initial guess vector
	:param N: Int - Number of iterations
	:return: np.array([1 x n]) - Solution vector
	"""
	
	D = np.diag( A )
	U = np.triu( A, k=1 )
	L = np.tril( A, k=-1 )
	if x is None:
		x = np.zeros( ( len( b ), 1 ) )
	
	for i in range( N ):
		for j in range( len( x ) ):
			x[ j ] = b[ j ] - np.dot( U[ j ], x )
			x[ j ] -= np.dot( L[ j ], x )
			x[ j ] = np.reciprocal( D[ j ] ) * x[ j ]
	
	return x
	


def main( ):
	A = np.eye( n ) * 3 - np.eye( n, k=1 ) - np.eye( n, k=-1 )
	b = np.ones( ( n, 1 ) )
	b[ 0 ] = 2; b[ -1 ] = 2
	
	x = jacobi_iteration( A, b, N=50 )
	print( "Jacobi iterator: " )
	print( x )
	
	s = np.linalg.solve( A, b )
	print( "Numpy linalg solver: " )
	print( s )
	
	
	print( "\n\n\n\n\n:::::\n\n\n\n\n" )
	
	
	AA = np.eye( n ) * 2 + np.eye( n, k=1 ) + np.eye( n, k=-1 )
	bb = np.zeros( ( n, 1 ) )
	bb[ 0 ] = 1; b[ -1 ] = -1
	
	y = jacobi_iteration( AA, bb, N=1000 )
	print( "Jacobi iterator: " )
	print( y )
	
	t = np.linalg.solve( AA, bb )
	print( "Numpy linalg solver: " )
	print( t )
	
	
	print( "\n\n\n\n\n:::::\n\n\n\n\n" )
	
	
	z = gauss_seidel_iteration( AA, bb, N=1000 )
	print( "Gauss-Seidel iterator: " )
	print( z )




if __name__ == "__main__":
	main( )

