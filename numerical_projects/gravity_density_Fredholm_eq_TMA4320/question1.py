## This program plots the solution to question 1 ##

import numpy as np
from matplotlib import pyplot as plt

# Define some things for the plotting
font = {'family' : 'normal', 'weight' : 'bold', 'size' : 17}
plt.rc('font', **font)

print("\n##### RUNNING PROGRAM q1 #####\n")

# Interval I = [a,b]
a=0; b= 1
a0=1/3; b0=2/3
acc=100
d1=0.025; d2=0.25; d3=2.5

def F(x, a, b, d):
	return (b-x) / (d*(d**2+(x-b)**2)**(1/2)) - (a-x) / (d*(d**2+(x-a)**2)**(1/2))

def plotting():
	xvalues = np.linspace(a,b,acc)
	yvalues1 = np.zeros(acc)
	yvalues2 = np.zeros(acc)
	yvalues3 = np.zeros(acc)
	for i in range(acc):
		yvalues1[i] = (F(xvalues[i], a0, b0, d1))
		yvalues2[i] = (F(xvalues[i], a0, b0, d2))
		yvalues3[i] = (F(xvalues[i], a0, b0, d3))
	plt.semilogy(xvalues, yvalues1, label=r'$d = 0.025$', lw=3)
	plt.semilogy(xvalues, yvalues2, label=r'$d = 0.25$', lw=3)
	plt.semilogy(xvalues, yvalues3, label=r'$d = 2.5$', lw=3)
	plt.legend(loc="best")
	plt.xlabel(r"$x$")
	plt.ylabel(r"$ln(F(x))$")
	plt.grid()
	plt.show()

plotting()