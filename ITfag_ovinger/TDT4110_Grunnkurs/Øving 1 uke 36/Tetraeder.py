import math

#importerer math for å bruke kvadratrot

h=float(input("Skriv inn en verdi for h: "))
a=(3/(math.sqrt(6)))*h

#setter variabelen a ved hjelp av input til h

A=math.sqrt(3)*a**2

print("Overflatearealet for en høyde lik",h,", er:", format(A, '.3f'))
#Formaterer med 3 desimalplasser slik at det er koherent med oppgaven.

V=(math.sqrt(2)*a**3)/(12)
print("Volumet for en høyde lik",h,", er:", format(V, '.3f'))
