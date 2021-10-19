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

x_verdier = [-0.19, -0.18, -0.17, -0.16, -0.15, -0.14, -0.13, -0.12, -0.11, -0.1, -0.09, -0.08, -0.07, -0.06, -0.05, -0.04, -0.03, -0.02, -0.01, 0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19]
malt_B1 = [2.48, 2.89, 3.37, 4, 4.73, 5.65, 6.74, 8.16, 9.96, 12.23, 15.03, 18.05, 22.88, 27.85, 33.37, 39.3, 44.94, 49.59, 52.16, 53.48, 52.32, 49.22, 44.53, 38.91, 32.95, 27.33, 22.15, 17.96, 14.6, 11.84, 9.72, 7.98, 6.62, 5.5, 4.62, 3.89, 3.3, 2.83, 2.43]
beregnet_B1 = [2.542, 2.939, 3.418, 4.001, 4.717, 5.602, 6.702, 8.079, 9.810, 11.993, 14.739, 18.170, 22.387, 27.420, 33.151, 39.226, 45.041, 49.852, 53.001, 54.092, 53.001, 49.852, 45.041, 39.226, 33.151, 27.420, 22.387, 18.170, 14.739, 11.993, 9.810, 8.079, 6.072, 5.062, 4.717, 4.001, 3.418, 2.939, 2.542]
malt_B2 = [2.75, 3.23, 3.8, 4.53, 5.37, 6.48, 7.8, 9.55, 11.66, 14.27, 17.73, 21.59, 26.12, 30.54, 35.03, 38.62, 40.93, 42.02, 42.31, 42.32, 42.29, 42.06, 41.06, 38.91, 35.2, 31.02, 26.22, 21.62, 17.68, 14.54, 11.73, 9.55, 7.87, 6.46, 5.41, 4.48, 3.79, 3.22, 2.73]
beregnet_B2 = [2.842, 3.313, 3.889, 4.598, 5.476, 6.573, 7.947, 9.675, 11.843, 14.545, 17.856, 21.794, 26.250, 30.923, 35.301, 38.805, 41.051, 42.093, 42.370, 42.390, 42.370, 42.093, 41.051, 38.805, 35.301, 30.923, 26.250, 21.794, 17.856, 14.545, 11.843, 9.675, 7.947, 6.573, 5.476, 4.598, 3.889, 3.313, 2.842]
malt_B3 = [4.15, 4.99, 6.04, 7.35, 8.96, 11.03, 13.63, 16.71, 20.21, 23.94, 27.68, 30.65, 32.2, 32.08, 30.54, 28.16, 25.53, 23.55, 21.96, 21.48, 21.96, 23.38, 25.58, 28.15, 30.58, 32.16, 32.24, 30.68, 27.71, 24.07, 20.17, 16.58, 13.53, 11.03, 8.95, 7.31, 5.99, 4.96, 4.12]
beregnet_B3 = [4.310, 5.164, 6.236, 7.586, 9.284, 11.409, 14.033, 17.184, 20.798, 24.636, 28.239, 30.977, 32.270, 31.893, 30.121, 27.585, 24.974, 22.815, 21.423, 20.945, 21.423, 22.815, 24.974, 27.585, 30.121, 31.893, 32.270, 30.977, 28.239, 24.636, 20.798, 17.184, 14.033, 11.409, 9.284, 7.586, 6.236, 5.164, 4.310]

delta_B1 = []
delta_B2 = []
delta_B3 = []

plussdiff1 = []
minusdiff1 = []
plussdiff2 = []
minusdiff2 = []
plussdiff3 = []
minusdiff3 = []

for i in range(len(x_verdier)):
    if x_verdier[i] != 0:
        delta_B1.append(math.sqrt(0.0039775510+12*((0.003)/(beregnet_B1[i]))**2)*beregnet_B1[i])
        delta_B2.append(math.sqrt(0.0039775510+12*((0.003)/(beregnet_B2[i]))**2)*beregnet_B2[i])
        delta_B3.append(math.sqrt(0.0039775510+12*((0.003)/(beregnet_B3[i]))**2)*beregnet_B3[i])
    else:
        delta_B1.append(math.sqrt(0.0039775510)*beregnet_B1[i])
        delta_B2.append(math.sqrt(0.0039775510)*beregnet_B2[i])
        delta_B3.append(math.sqrt(0.0039775510)*beregnet_B3[i])
#0.0639775510

for i in range(len(x_verdier)):
    plussdiff1.append(beregnet_B1[i]+delta_B1[i])
    minusdiff1.append(beregnet_B1[i]-delta_B1[i])

    plussdiff2.append(beregnet_B2[i]+delta_B2[i])
    minusdiff2.append(beregnet_B2[i]-delta_B2[i])

    plussdiff3.append(beregnet_B3[i]+delta_B3[i])
    minusdiff3.append(beregnet_B3[i]-delta_B3[i])

plt.plot(x_verdier, plussdiff1, label='Standardfeil', linewidth='3')
plt.plot(x_verdier, minusdiff1, label='Standardfeil', linewidth='3')
plt.plot(x_verdier, malt_B1, label='Målte verdier', linewidth='3')
plt.title('Måleverdier ift. standardfeil - forsøk 2 - a1=R/2', size='30')
plt.xlabel('x i meter', size='20')
plt.ylabel('B i gauss (10^4 T)', size='20')
ticks_font = fontmg.FontProperties(family='Helvetica', style='normal', size='30', weight='normal', stretch='normal')
plt.legend(prop={'size':30})
plt.grid()
plt.show()

plt.plot(x_verdier, plussdiff2, label='Standardfeil', linewidth='3')
plt.plot(x_verdier, minusdiff2, label='Standardfeil', linewidth='3')
plt.plot(x_verdier, malt_B2, label='Målte verdier', linewidth='3')
plt.title('Måleverdier ift. standardfeil - forsøk 2 - a2=R', size='30')
plt.xlabel('x i meter', size='20')
plt.ylabel('B i gauss (10^4 T)', size='20')
ticks_font = fontmg.FontProperties(family='Helvetica', style='normal', size='30', weight='normal', stretch='normal')
plt.legend(prop={'size':30})
plt.grid()
plt.show()

plt.plot(x_verdier, plussdiff3, label='Standardfeil', linewidth='3')
plt.plot(x_verdier, minusdiff3, label='Standardfeil', linewidth='3')
plt.plot(x_verdier, malt_B3, label='Målte verdier', linewidth='3')
plt.title('Måleverdier ift. standardfeil - forsøk 2 - a3=2R', size='30')
plt.xlabel('x i meter', size='20')
plt.ylabel('B i gauss (10^4 T)', size='20')
ticks_font = fontmg.FontProperties(family='Helvetica', style='normal', size='30', weight='normal', stretch='normal')
plt.legend(prop={'size':30}, loc='lower center')
plt.grid()
plt.show()

