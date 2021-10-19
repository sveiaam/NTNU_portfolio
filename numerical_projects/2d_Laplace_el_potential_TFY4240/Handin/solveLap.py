from numpy import *
from matplotlib.pyplot import *


#Plotting text
font = {'family' : 'sans-serif', 'weight' : 'bold', 'size' : 15}
rc('font', **font)


def executePlotting(Q=50, N=4, save=False):
	'''
	
	:param Q: Int; number of plotting and integrating points
	:param N: Int; number of Fourier coefficients
	:param save: Bool; saving images as PDF
	:return: None
	'''
	# Create grid
	xvals = linspace(0, 1, Q)
	yvals = linspace(0, 1, Q)
	k = len(xvals)
	l = len(yvals)
	
	# Create V_0
	v1 = lambda x: 1 + (tanh(1 - 6*x**2))**2
	V0 = array([v1(x) for x in xvals])
	
	
	def numint(n):
		s = 0
		for i in range(k):
			s += V0[i] * sin(n*pi*xvals[i]) / l
		return s
	
	# Create Fourier coefficients
	Fcoeffs = zeros(N)
	for n in range(1, N+1):
		Fcoeffs[n-1] = numint(n) / sinh(n*pi)
	
	def V(x, y):
		v = 0
		for n in range(1, N+1):
			v += Fcoeffs[n-1] * sin(n*pi*x) * sinh(n*pi*y)
		return 2*v
	
	# Create points for plotting V(x,y)
	zvals = zeros((k, l))
	for i in range(l):
		for j in range(k):
			zvals[i, j] = V(xvals[j], yvals[i])
	
	# Create E
	E = negative(gradient(zvals))
	
	# Plot
	plot(xvals, V0, lw=4)
	grid()
	title(r"$V_{0}(\xi)$")
	xlabel(r"$\xi$")
	ylabel(r"$V_{0}$")
	gca().set_aspect("equal", adjustable="box")
	if save:
		savefig("plotV0.pdf")
	show()
	
	plot(xvals, zvals[-1], lw=4)
	grid()
	title(r"$V(\xi, \eta = 1)$ with %s Fourier components"%N)
	xlabel(r"$\xi$")
	ylabel(r"$V(\eta = 1)$")
	#gca().set_aspect("equal", adjustable="box")
	if save:
		savefig("plotVy1.pdf")
	show()
	
	contourf(xvals, yvals, zvals, 100)
	title(r"$V(\xi, \eta)$")
	xlabel(r"$\xi$")
	ylabel(r"$\eta$")
	gca().set_aspect("equal", adjustable="box")
	colorbar()
	if save:
		savefig("plotVxy.pdf")
	show()
	
	q = int(Q/10)
	quiver(xvals[0::q], yvals[0::q], E[1, 0::q, 0::q], E[0, 0::q, 0::q], width=0.015, headwidth=4, pivot="mid")
	title(r"$\vec{E}(\xi, \eta)$")
	xlabel(r"$\xi$")
	ylabel(r"$\eta$")
	gca().set_aspect("equal", adjustable="box")
	if save:
		savefig("plotExy.pdf")
	show()


def main():
	Q = 500 #Global plotting parameter
	N = 4 #Number of Fourier components
	save = True # Set to True to save the images as PDF in current folder
	
	executePlotting(Q, N, save)


if __name__ == "__main__":
	main()
