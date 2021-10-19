from numpy import *
from matplotlib.pyplot import *

save = True

font = {'family' : 'sans-serif', 'weight' : 'bold', 'size' : 15}
rc('font', **font)

background = loadtxt("background.txt", float)
breath = loadtxt("breath.txt", float)
polyethylene = loadtxt("polyethylene.txt", float)
siliconcarbide = loadtxt("siliconcarbide.txt", float)


plot(background[:,0], background[:,1])
xlim(background[0,0], background[-1,0])
title("Background")
xlabel(r"$\sigma [\mathrm{cm}^{-1}]$")
ylabel(r"Transmission $[\%]$")
grid()
tight_layout()
if save:
	savefig("backgroundplot.pdf")
show()

plot(breath[:,0], breath[:,1])
xlim(breath[0,0], breath[-1,0])
title("Breath")
xlabel(r"$\sigma [\mathrm{cm}^{-1}]$")
ylabel(r"Transmission $[\%]$")
grid()
tight_layout()
if save:
	savefig("breathPlot.pdf")
show()


polyethylene_lines = array([2875, 1450, 725])
polyethylene_names = array([r"$\sigma_{1}$", r"$\sigma_{2}$", r"$\sigma_{3}$"])

plot(polyethylene[:,0], polyethylene[:,1])
xlim(4000, polyethylene[-1,0])
for i in range(len(polyethylene_lines)):
	axvline(x=polyethylene_lines[i], color='red', lw=4, ls=':')
	text(polyethylene_lines[i]-40,0, polyethylene_names[i])
title("Polyethylene")
xlabel(r"$\sigma [\mathrm{cm}^{-1}]$")
ylabel(r"Transmission $[\%]$")
grid()
tight_layout()
if save:
	savefig("polyethylenePlot.pdf")
show()


siliconcarbide_lines = array([930, 830])
siliconcarbide_names = array([r"$\sigma_{\mathrm{LO}}$", r"$\sigma_{\mathrm{TO}}$"])

plot(siliconcarbide[:,0], siliconcarbide[:,1])
xlim(1200, siliconcarbide[-1,0])
for i in range(len(siliconcarbide_lines)):
	axvline(x=siliconcarbide_lines[i], color='red', lw=4, ls=':')
	text(siliconcarbide_lines[i] - 10, 7, siliconcarbide_names[i])
title("Silicon carbide")
xlabel(r"$\sigma [\mathrm{cm}^{-1}]$")
ylabel(r"Transmission $[\%]$")
grid()
tight_layout()
if save:
	savefig("siliconcarbidePlot.pdf")
show()
