import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as col

def NewtonsMethod(x0, delta):   #Beregner f(x) = x^3-1 = 0 med startpunkt x0 og toleranse delta
	counter = 0
	xi = x0
	while True:
		counter += 1
		xi1 = xi - (xi**3-1)/(3*xi**2)
		diff = abs(xi-xi1)
		#print("%-0s %3.0f" % ("iter.", counter) + "   ||  ", "%-4s %4.12f" % ("x_i =", xi) + "   ||  ", "%-4s %4.12f" % ("diff =", diff))
		if diff < delta:
			break
		xi = xi1
	return xi

#Complex roots of f(x) = x^3 - 1
r1 = 1
r2 = 1/2 * (-1 + 1j*np.sqrt(3))
r3 = 1/2 * (-1 - 1j*np.sqrt(3))
#Tolerance
tol = 10e-8
#Accuracy of plot
acc = 200

def main():
	re = np.linspace(-2, 2, acc)
	im = np.linspace(-2, 2, acc)
	size = (acc, acc)
	map = np.zeros(size)
	for b in range(acc):
		for a in range (acc):
			root = NewtonsMethod(re[a] + 1j*im[b], tol)
			if np.absolute(root - r1) < tol:
				map[b, a] = 1
			if np.absolute(root - r2) < tol:
				map[b, a] = 2
			if np.absolute(root - r3) < tol:
				map[b, a] = 3

	fig, ax = plt.subplots()

	colors = ["yellow", "red", "green", "blue"]
	bounds = [0, 1, 2, 3, 4]
	cmap = col.ListedColormap(colors)
	norm = col.BoundaryNorm(bounds, cmap.N)

	ax.matshow(map, extent=[-2, 2, -2, 2], cmap=cmap, norm=norm, interpolation='none')

	plt.title("Convergence point of different initial values with Newtons method on f(x) = x^3 - 1 = 0")
	plt.xlabel("Re", size='20')
	plt.ylabel("Im", size='20')
	plt.show()


main()

# yellow = divergence, red = conv. to r1, green = conv. to r2, blue = conv. to r3
