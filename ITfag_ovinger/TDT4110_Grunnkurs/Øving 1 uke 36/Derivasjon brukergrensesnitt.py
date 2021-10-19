import math #importerer math for å få tilgang til sin(...)

#Lager variablene h og x
x=float(input("Skriv inn en verdi for x: "))
h=float(input("Skriv inn en verdi for h: "))

f1=math.sin(x) # sin(x) har verdi sin(x) i punktet x.
f2=math.sin(x+h)

print(format(f1, '.5f'))
print(format(f2, '.5f'))

derivert=(f2-f1)/h
print("Den deriverte er omtrent:", '"'+str(format(derivert,'.3f'))+'"',"for x=",x,", og h=",h,"!")
#Gjør om til string for å kunne ha "" tegn rundt svaret når det printes.
    #(Det er i hvert fall den metoden jeg har lært meg)
