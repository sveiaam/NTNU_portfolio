#Største felles divisor
def gcd(a,b):
	if a % b == 0:
		return b
	else:
		return gcd(b, a%b)

#Antall divisorer av n
def tau(n):
	k = 0
	for i in range(1, n+1):
		if n%i == 0:
			k += 1
	return k

#Sum av divisorene til n
def sigma(n):
	k = 0
	for i in range(1, n+1):
		if n%i == 0:
			k += i
	return k

#Antall k<n som er relativt primiske til n
def phi(n):
	k = 1
	for i in range(2, n+1):
		if gcd(n, i) == 1:
			k += 1
	return k

#True om n er primtall
def primtest(n):
	if n == 1:
		return False
	for i in range(2,n):
		if gcd(n, i) != 1:
			return False
	return True

#Hjelpefunksjon
def euklid(a,b):
	q = a // b
	r = a % b
	if r == 0:
		return b, 1, 1-q
	else:
		d, x, y = euklid(b,r)
		return d, y, x-q*y

#Returnerer en liste av alle løsninger x (av ax kongruent b (mod m)) som er kongruente mod m/d
def linear_kongruens(a, b, m):
	d, u, v = euklid(a,m)
	if b % d != 0:
		return []
	M = int(m/d)
	B = int(b/d)
	x0 = (u*B) % M
	return [x0 + i * M for i in range(d)]

#Returnerer inversen x av (ax kongruent med 1 (mod m))
def invers(a, m):
	losninger = linear_kongruens(a, 1, m)
	if len(losninger) == 0:
		return None
	return losninger[0]

#returnerer n!
def factorial(n):
	if n == 0 or n == 1:
		return 1
	else:
		return n * factorial(n-1)

#returnerer n:C:k
def binomialkoeff(n, k):
	if k < 0 or k > n:
		return 0
	else:
		return int(factorial(n) / (factorial(k)*factorial(n-k)))

