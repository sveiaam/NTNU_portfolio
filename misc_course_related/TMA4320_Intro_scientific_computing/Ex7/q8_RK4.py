import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as ani


s = 10
r = 28
b = 8/3


def RK4( f, tmin, tmax, y0 = None, h = 0.1 ):
	"""
	
	:param f: Function or set of functions to be evaluated
	:param tmin: float; minimal t to evaluate functions
	:param tmax: float; maximum t to evaluate functions
	:param y0: f()-param-type; initial conditions
	:param h: float; step length
	:return:
	"""
	
	if y0 is None:
		print( "ERROR: insert initial guess" )
		return False
	
	timelist = np.arange( tmin, tmax+h, h )
	ylist = np.zeros( ( len( timelist ), len( y0 ) ) )
	y = y0
	
	ylist[ 0 ] = y
	
	for i in range( 1, len( timelist ) ):
		s1 = f( y )
		s2 = f( y + h/2 * s1 )
		s3 = f( y + h/2 * s2 )
		s4 = f( y + h * s3 )
		
		y = y + h/6 * ( s1 + 2*s2 + 2*s3 + s4 )
		
		ylist[ i ] = y
	
	return ylist


def lorentz( w ):
	return np.array( [
		-s*w[ 0 ] + s*w[ 1 ],
		-w[ 0 ]*w[ 2 ] + r*w[ 0 ] - w[ 1 ],
		w[ 0 ]*w[ 1 ] - b*w[ 2 ]
		] )


def main( ):
	tmin = 0
	y0 = np.array( [ 5, 5, 5 ] )
	y1 = np.array( [ 20, 0, -10] )
	h = 0.001
	tmax1 = 10
	tmax2 = 20
	
	trajectory1 = RK4( lorentz, tmin, tmax2, y0, h )
	trajectory2 = RK4( lorentz, tmin, tmax2, y1, h )
	
	
	x1, y1, z1 = trajectory1.T
	x2, y2, z2 = trajectory2.T
	
	fig = plt.figure( )
	ax = fig.add_subplot( 1, 2, 1, projection='3d' )
	ax.plot( x1, y1, z1 )
	
	ax = fig.add_subplot( 1, 2, 2, projection='3d' )
	ax.plot( x2, y2, z2 )
	
	plt.show( )
	
	

if __name__ == "__main__":
	main( )

"""

It would appear that changing the initial conditions slightly (or even considerably) does not
... affect the plot greatly. Such, the Lorenz equations can be described as an attractor

"""

