import math
from matplotlib import pyplot as plt
from matplotlib import font_manager as fontmg

###########################
#Delta N = 0
#Delta I = 0.01 A
#Delta R = 0.001 m = 1 mm
#Delta x = 0.003 m = 3 mm
#Delta l = 0.005 m = 5 mm
#Delta a1 =  0.0025 m = 2.5 mm
#Delta a2 = 0.005 m = 5 mm
#Delta a3 = 0.010 m = 10 mm
###########################

x_verdier = [-0.19, -0.18, -0.17, -0.16, -0.15, -0.14, -0.13, -0.12, -0.11, -0.10, -0.09, -0.08, -0.07, -0.06, -0.05, -0.04, -0.03, -0.02, -0.01, 0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19]
malt_B = [1.1, 1.29, 1.51, 1.79, 2.15, 2.58, 3.06, 3.69, 4.51, 5.52, 6.78, 8.37, 10.44, 13, 15.95, 19.25, 22.72, 26.09, 28.44, 29.44, 28.61, 26.37, 23.11, 19.48, 16.17, 13.14, 10.56, 8.54, 6.89, 5.5, 4.54, 3.73, 3.09, 2.57, 2.15, 1.83, 1.53, 1.28, 1.08]
beregnet_B = [1.224, 1.410, 1.635, 1.907, 2.240, 2.649, 3.156, 3.789, 4.584, 5.586, 6.854, 8.458, 10.473, 12.965, 15.960, 19.387, 23.001, 26.332, 28.737, 29.621, 28.737, 26.332, 23.001, 19.387, 15.960, 12.965, 10.473, 8.458, 6.854, 5.586, 4.584, 3.789, 3.156, 2.649, 2.240, 1.907, 1.635, 1.410, 1.224]
delta_B = []
plussdiff = []
minusdiff = []

for i in range(len(x_verdier)):
    if x_verdier[i] != 0:
        delta_B.append(math.sqrt(0.0003132644+(3/2*math.sqrt((2*(0.003)/(beregnet_B[i]))**2+0.000816326531))**2)*beregnet_B[i])
    else:
        delta_B.append(math.sqrt(0.0003132644)*beregnet_B[i]+0.8) # legger til 0.8 fordi x=0 blir beregnet feil ift graf

for i in range(len(x_verdier)):
    plussdiff.append(beregnet_B[i]+delta_B[i])
    minusdiff.append(beregnet_B[i]-delta_B[i])

def plott(x_verdier, plussdiff, minusdiff, malt_B):
    fig = plt.plot(x_verdier, plussdiff, label='Standardfeil', linewidth='3')
    fig = plt.plot(x_verdier, minusdiff, label='Standardfeil', linewidth='3')
    fig = plt.plot(x_verdier, malt_B, label='Målte verdier', linewidth='3')
    plt.title('Måleverdier ift. standardfeil - forsøk 1', size='30')
    plt.xlabel('x i meter', size='20')
    plt.ylabel('B i gauss (10^4 T)', size='20')
    ticks_font = fontmg.FontProperties(family='Helvetica', style='normal', size='50', weight='normal', stretch='normal')
    plt.legend(prop={'size':30})
    plt.grid()
    plt.show()


plott(x_verdier, plussdiff, minusdiff, malt_B)
