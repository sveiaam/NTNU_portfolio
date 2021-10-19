from matplotlib import pyplot as plt
import numpy as np
from lib import read_csv as rd
import scipy.stats

m0 = 6.093 #gram
t_al = 4.16666667   #tid der al ble lagt til
t_kok = 5.1666667   #tid der al kokte
Theta = 315.25
n = 0.233   #mol aluminium
R = 8.314472   #universell gasskonstant
T0_min = 294
T0_max = 296
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
def Delta_Q_min(Theta):
	return 3*n*R*(T0_min * Epsilon(Theta/T0_min) - Tf * Epsilon(Theta/Tf))
def Delta_Q_max(Theta):
	return 3*n*R*(T0_max * Epsilon(Theta/T0_max) - Tf*Epsilon(Theta/Tf))

deltaQ_min = Delta_Q_min(Theta)
print("Delta Q (min) = "+str(deltaQ_min))
deltaQ_max = Delta_Q_max(Theta)
print("Delta Q (max) = "+str(deltaQ_max))

delta_m = (f1(t_al)-f2(t_al)  +  f1(t_kok)-f2(t_kok))/2
print("delta m = "+str(delta_m))
