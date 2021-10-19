hemmelig_ord=input("Skriv inn det hemmelige ordet: ")

skjult=list(hemmelig_ord) #Skriver tegnene i skjult_ord som entryene i en liste.
x=len(skjult) #Finner antall elementer i lista skjult som verdien x.
vist=['*']*x    #Lager en liste med samme antall elementer som hemmelig_ord, men alle tegn er *

print(skjult)
print(x)
print(vist)

gjett=input("skriv inn en bokstav: ")
if gjett in skjult:
    print(gjett,"er en riktig bokstav")
    posisjon = [i for i,j in enumerate(skjult) if j == gjett] #posisjon er en liste over indeksplasseringene til de(t) tall(ene) som ble gjettet
    vist[posisjon]=gjett

print(posisjon)

'''for i in enumerate(skjult):
    if i == gjett
##
posisjon=skjult.index(gjett)
'''