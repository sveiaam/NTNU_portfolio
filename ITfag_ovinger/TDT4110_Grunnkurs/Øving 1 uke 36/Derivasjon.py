import math #importerer math for å få tilgang til sin(...)

#Lager variablene h og x
h=10**(-3)
x=3.14

f1=math.sin(x) # sin(x) har verdi sin(x) i punktet x.
f2=math.sin(x+h)

print(format(f1, '.5f'))
print(format(f2, '.5f'))
#Disse to er kun for å sjekke at verdien av disse stemmer. Når x=math.pi er
    #verdien som forventet, men med x=3.14 er det en betydelig feilmargin.

derivert=(f2-f1)/h
print(derivert)
