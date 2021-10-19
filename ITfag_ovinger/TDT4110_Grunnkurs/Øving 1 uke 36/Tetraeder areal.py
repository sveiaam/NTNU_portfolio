import math

#importerer math for å bruke kvadratrot

h=float(input("Skriv inn en verdi for h: "))
a=(3/(math.sqrt(6)))*h

#setter variabelen a ved hjelp av input til h

A=math.sqrt(3)*a**2

print("Overflatearealet er", format(A, '.3f'))
#Formaterer med 3 desimalplasser slik at det er koherent med oppgaven.
