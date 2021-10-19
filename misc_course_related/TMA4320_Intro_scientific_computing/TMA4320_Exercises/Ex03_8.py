def midpointNC(f, a, b, N):
	#Expects a function f(x), interval [a,b] and N number of panels
	#Returns int_a^b f(x) dx evaluated with midpoint quadrature on the N midpoints in [a,b]
	h = (a-b) / N
	counter = 0
	for i in range(N):
		counter += f(a+h/2+i*h)
	return h * counter

# The above is temporary, will move somewhere appropriate
