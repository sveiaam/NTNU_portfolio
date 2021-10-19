from matplotlib import pyplot as plt
import matplotlib as mp
import numpy as np
from lib import read_csv as rd
import scipy.stats

#Noen konstanter
m0 = 6.093 #Aluminiumets masse i gram
t_al = 4.16666667   #tid der al ble lagt til i min
t_kok = 5.1666667   #tid der al kokte i min
Theta = 318.5
n = 0.233   #antall mol aluminium
R = 8.314472   #universell gasskonstant
T0 = 295 #romtemp i kelvin
Tf = 77 #kokepkt for N2 i kelvin

#Leser inn massedata fra excelark og trekker fra den ekstra vekten fra aluminimumets og trådens masse
data = rd.read_csv('lab2_tabell.csv')
for i in range(5,11):
	data[i,1] = data[i,1]-m0

#Deler opp dataene i to mengder - en før og en etter at aluminiumet ble lagt til
set1 = np.zeros((5,2))
set2 = np.zeros((5,2))
for i in range(0,5):
	set1[i,0] = data[i,0]
	set1[i,1] = data[i,1]
	set2[i,0] = data[i+5, 0]
	set2[i,1] = data[i+5, 1]
set1 = np.array(set1)
set2 = np.array(set2)

#Foretar lineær regresjon på de to delmengdene
#...for å finne rette linjer, f1(x) og f2(x) som representerer massetapsratene før og etter alu
slope1, intercept1, rvalue1, pvalue1, stderr1 = scipy.stats.linregress(set1[:,0], set1[:,1])
slope2, intercept2, rvalue2, pvalue2, stderr2 = scipy.stats.linregress(set2[:,0], set2[:,1])
def f1(x):
	return slope1*x + intercept1
def f2(x):
	return slope2*x + intercept2

#Lager en mengde verdier for tiden (i minutter) for å plotte linjene f1 og f2 mot
x = np.linspace(0,11, 200)

#Definerer en funksjon som gir et teoretisk resultat for delte Q for en verdi av Theta
def Epsilon(y):
	return y/(np.e**y-1)
def Delta_Q(Theta):
	return 3*n*R*(T0 * Epsilon(Theta/T0) - Tf * Epsilon(Theta/Tf))

#Printer til skjermen hva delta Q og delta m er
deltaQ = Delta_Q(Theta)
print("Delta Q ="+str(deltaQ))
delta_m = (f1(t_al)-f2(t_al)  +  f1(t_kok)-f2(t_kok))/2
print("delta m = "+str(delta_m))

#Her ville man beregnet en eksperimentell verdi for delta Q med formelen delta Q = L * delta m
#Tilpasser så Theta slik at de to uttrykkene over er like

#Plotter figuren med måledataene
plt.figure()
#De rette regresjonslinjene
plt.plot(x, f1(x), lw=5, label='Masse av N2 før Al-tilsetning')
plt.plot(x, f2(x), lw=5, label='Masse av N2 etter Al-tilsetning')
#Tidsakser
plt.plot((t_al, t_al),(35, 65), lw=5, color='k', label='Tilsetning av, og T-utjevning i Al')
plt.plot((t_kok, t_kok),(35,65), lw=5, color='k')
#Eksperimentelle verdier
plt.plot(data[:,0], data[:,1], marker='o', ms=12, ls='', label='Eksperimentelle måleverdier', markeredgewidth=3)
#Spesifikasjoner for plottet
#plt.title('Masseutvikling over tid', size=34)
plt.xlabel('Tid i minutter', size=28)
plt.ylabel('Masse i gram', size=28)
plt.legend(fontsize=26)
plt.grid()
mp.rcParams.update({'font.size': 24})
plt.show()

#Printer tilleggsinformasjon for å kunne gi en analytisk beskrivelse av regresjonslinjene
#slope1 og slope2 er stigningstallene, konst1 og konst2 er konstantleddene
print("slope1 ="+str(slope1))
print("konst1 ="+str(intercept1))
print("slope2 ="+str(slope2))
print("konst2 ="+str(intercept2))


# (1) = Projisert masse av N2 før tilsetning av Al
# (2) = Projisert masse av N2 etter tilsetning av Al
# (3) = Tilsetning av, og temperaturutjevning i Al
# (4) = Eksperimentelle måleverdier