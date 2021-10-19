def f(m, k):
	return (m+k) % 32
def g(c, k):
	return (c-k) % 32

Tabell = ['_','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','Æ','Ø','Å','?',',']
c = [18,0,11,10,15,28,10,3,24,14,22,19,24,17,29,16,11,28,17,15,24,10,14,19,24,8]

def number_to_letter(L):
	L2 = []
	for i in L:
		L2.append(Tabell[i])
	return L2

def hacking(kode):
	for i in range(32):
		L = []
		for j in range(len(kode)):
			L.append(g(kode[j], i))
		print(str(''.join(number_to_letter(L))) + '    ' + str(i))

hacking(c)