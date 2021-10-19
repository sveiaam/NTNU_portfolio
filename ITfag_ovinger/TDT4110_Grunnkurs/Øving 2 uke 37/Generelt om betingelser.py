a=float(input("Skriv inn tall a: "))
b=float(input("Skriv inn tall b: "))

multiplum=a*b
summering=a+b

if multiplum < summering:
    print("Produktet av a og b,",format(multiplum, '.3f'),"er den operasjonen som gir minst resultat.\n\n")
elif multiplum > summering:
    print("Summen av a og b,",format(summering, '.3f'),"er den operasjonen som gir minst resultat.\n\n")
else:
    print("Summen og produktet av a og b er like store.")

input("Trykk enter for å fortsette\n")

x=1
while x==1:
    svar = input("Hva er 3*4?   ")
    if str.isdigit(svar) == True:
        svar_float=float(svar)
        if svar_float == 12:
            print("Svaret er riktig")
            x=2
        else:
            print("Svaret er feil, prøv igjen.\n")
    else:
        print("Svaret er feil, prøv igjen.\n")
