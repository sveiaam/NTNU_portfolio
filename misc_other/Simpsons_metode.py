def simpson(funksjon, start, slutt, n):
	count = funksjon(start) + funksjon(slutt)
	h = float((slutt-start)/n)
	x = start+h
	for i in range(1, int(n/2+1)):
		count += 4*funksjon(x)
		x += 2*h
	x = start + 2*h
	for i in range(1, int(n/2)):
		count += 2*funksjon(x)
		x += 2*h
	return(h/3)*count
