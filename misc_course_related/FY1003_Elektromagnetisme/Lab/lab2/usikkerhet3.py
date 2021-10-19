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

x_verdier = [-0.1, -0.09, -0.08, -0.07, -0.06, -0.05, -0.04, -0.03, -0.02, -0.01, 0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49]
malt_B = [0.69, 0.78, 0.91, 1.09, 1.32, 1.62, 2.01, 2.53, 3.23, 4.14, 5.22, 6.41, 7.53, 8.5, 9.3, 9.9, 10.36, 10.69, 10.93, 11.12, 11.26, 11.37, 11.45, 11.51, 11.56, 11.6, 11.63, 11.65, 11.66, 11.67, 11.68, 11.68, 11.67, 11.65, 11.64, 11.61, 11.58, 11.54, 11.49, 11.42, 11.33, 11.21, 11.05, 10.85, 10.56, 10.2, 9.71, 9.02, 8.18, 7.13, 5.97, 4.8, 3.79, 2.96, 2.33, 1.85, 1.5, 1.22, 1.02, 0.88]
beregnet_B = [0.588, 0.706, 0.858, 1.057, 1.322, 1.678, 2.159, 2.802, 3.638, 4.662, 5.807, 6.953, 7.976, 8.811, 9.453, 9.932, 10.287, 10.549, 10.745, 10.894, 11.007, 11.095, 11.163, 11.216, 11.257, 11.289, 11.313, 11.330, 11.342, 11.348, 11.349, 11.345, 11.337, 11.322, 11.302, 11.274, 11.238, 11.191, 11.131, 11.054, 10.954, 10.825, 10.654, 10.427, 10.123, 9.711, 9.155, 8.419, 7.486, 6.389, 5.226, 4.129, 3.195, 2.458, 1.900, 1.487, 1.180, 0.950, 0.777, 0.643]
delta_B = []
plussdiff = []
minusdiff = []

for i in range(len(x_verdier)):
    if x_verdier[i] != 0:
        delta_B.append(math.sqrt(0.000417346033+5*((0.003)/(beregnet_B[i]))**2)*beregnet_B[i])
    else:
        delta_B.append(math.sqrt(0.000417346033)*beregnet_B[i])

for i in range(len(x_verdier)):
    plussdiff.append(beregnet_B[i]+delta_B[i])
    minusdiff.append(beregnet_B[i]-delta_B[i])

def plott(x_verdier, plussdiff, minusdiff, malt_B):
    plt.plot(x_verdier, plussdiff, label='Standardfeil', linewidth='3')
    plt.plot(x_verdier, minusdiff, label='Standardfeil', linewidth='3')
    plt.plot(x_verdier, malt_B, label='Målte verdier', linewidth='3')
    plt.title('Måleverdier ift. standardfeil - forsøk 3', size='30')
    plt.xlabel('x i meter', size='20')
    plt.ylabel('B i gauss (10^4 T)', size='20')
    ticks_font = fontmg.FontProperties(family='Helvetica', style='normal', size='30', weight='normal', stretch='normal')
    plt.legend(prop={'size':30}, loc='lower center')
    plt.grid()
    plt.show()

plott(x_verdier, plussdiff, minusdiff, malt_B)
