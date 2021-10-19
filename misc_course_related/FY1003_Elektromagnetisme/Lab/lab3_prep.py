import math
from matplotlib import pyplot as plt
from matplotlib import font_manager as fontmg

r_list = []
B_list = []
B = 0
dB = 0.00001
U = 20

while B<15*10**(-4):
    B+=dB
    r_list.append(1/(B*10**(-4))*math.sqrt((2*U)/(1.7588*10**11)))
    B_list.append(B)

plt.plot(B_list, r_list, linewidth='3')
plt.title('r avhengig av B med U = 20V', size='25')
plt.xlabel('B', size='15')
plt.ylabel('r', size='15')
ticks_font = fontmg.FontProperties(family='Helvetica', style='normal', size='30', weight='normal', stretch='normal')
plt.grid()
plt.show()