#a)
total=0
x=0
while x<=100:
    total +=x
    x+=1    #Denne rekkefølgen er viktig så den ikke legger til 101 for mye.

print("Summen av de 100 første tallene er",total)


#b)
produkt=1
y=0
n=0
while produkt <= 1000:
    n+=1
    y+=1
    produkt=produkt*y

print("\nProduktet av de",n,"første naturlige tall blir",produkt)


#c)
def galtsvar():
    print("Svaret er galt.\n")
while True:
    print("Hva er 3*4?")
    svar=input("Svar:    ")
    if str.isdigit(svar):
        svar_int=int(svar)
        if svar_int == 12:
            break
        else:
            galtsvar()
    else:
        galtsvar()
print("Svaret er riktig.")
