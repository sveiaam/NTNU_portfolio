import numpy as np

def fwd_Euler( f, tmin, tmax, h, y0=None ):
	
	if y0 is None:
		y0 = 0.
	
	n = int( ( tmax - tmin ) / h )
	w = np.zeros( n + 1 )
	w[ 0 ] = y0
	
	for i in range( 1, n ):
		w[ i ] = w[ i - 1 ] + h * f( w[ i - 1 ], tmin + n*h )
	
	return w


def fwd_Trapezoid( f, tmin, tmax, h, y0=None ):
	
	if y0 is None:
		y0 = 0.
	
	n = int( ( tmax - tmin ) / h )
	w = np.zeros( n + 1 )
	w[ 0 ] = y0
	
	for i in range( 1, n ):
		w[ i ] = w[ i-1 ] + h/2 * ( f( w[ i-1 ], tmin+n*h ) + f( w[ i-1 ] + h*f( w[ i-1 ], tmin+n*h ), tmin+n*h+h ) )
	
	return w


def yprime( w, t ):
	return 4 * t - 2 * w

def main( ):
	h = 1/4
	tmin = 0
	tmax = 1
	
	a = fwd_Euler( yprime, tmin, tmax, h )
	print( a )
	b = fwd_Trapezoid( yprime, tmin, tmax, h )
	print( b )
	


if __name__ == "__main__":
	main( )

