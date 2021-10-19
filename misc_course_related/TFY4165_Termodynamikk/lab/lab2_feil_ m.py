from matplotlib import pyplot as plt
import numpy as np
from lib import read_csv as rd
import scipy.stats

m0 = 6.093 #gram
t_al = 4.16666667   #tid der al ble lagt til
t_kok = 5.1666667   #tid der al kokte
Theta_max = 302.25
Theta_min = 335
n = 0.233   #mol aluminium
R = 8.314472   #universell gasskonstant
T0 = 295 #romtemp i kelvin
Tf = 77 #kokepkt for N2

data = rd.read_csv('lab2_tabell.csv')
for i in range(5,11):
	data[i,1] = data[i,1]-m0

set1 = np.zeros((5,2))
set2 = np.zeros((5,2))
for i in range(0,5):
	set1[i,0] = data[i,0]
	set1[i,1] = data[i,1]
	set2[i,0] = data[i+5, 0]
	set2[i,1] = data[i+5, 1]
set1 = np.array(set1)
set2 = np.array(set2)

slope1, intercept1, rvalue1, pvalue1, stderr1 = scipy.stats.linregress(set1[:,0], set1[:,1])
slope2, intercept2, rvalue2, pvalue2, stderr2 = scipy.stats.linregress(set2[:,0], set2[:,1])

def f1(x):
	return slope1*x + intercept1
def f2(x):
	return slope2*x + intercept2
x = np.linspace(0,10, 200)

def Epsilon(y):
	return y/(np.e**y-1)
def Delta_Q(Theta):
	return 3*n*R*(T0 * Epsilon(Theta/T0) - Tf * Epsilon(Theta/Tf))

delta_max = f1(t_al)-f2(t_al)
print("delta m (max) = "+str(delta_max))
delta_min = f1(t_kok)-f2(t_kok)
print("delta m (min) = "+str(delta_min))

deltaQ_max = Delta_Q(Theta_max)
print("Delta Q (max) ="+str(deltaQ_max))
deltaQ_min = Delta_Q(Theta_min)
print("Delta Q (min) ="+str(deltaQ_min))
