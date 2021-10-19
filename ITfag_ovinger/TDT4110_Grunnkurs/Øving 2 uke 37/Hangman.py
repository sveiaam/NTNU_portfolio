#Samle input
'''
hemmelig_ord=str(input("Skriv inn løsningsordet: "))
x=1
while x==1:
    antall_liv_str=input("\nSkriv inn hvor mange 'liv' spilleren skal ha: ")
    if str.isdigit(antall_liv_str)==True:
        antall_liv=int(antall_liv_str)
        x=2
    else:
        print("Skriv inn et gyldig antall liv (heltall).\n")

skjult=list(hemmelig_ord) #Skriver tegnene i skjult_ord som entryene i en liste.
ordlengde=len(skjult) #Finner antall elementer i lista skjult som verdien x.
vist=["*"]*ordlengde #Lager en liste med samme antall elementer som hemmelig_ord, men alle tegn er *


while True:
    print(vist)
    gjett=input("Gjett en bokstav: ")
    if gjett == hemmelig_ord:
        break
    elif gjett in skjult:
        print(gjett,"er en av bokstavene i ordet.")
        posisjon = [i for i, j in enumerate(skjult) if j == gjett]
        # posisjon er en liste over indeksplasseringene til de(t) tall(ene) som ble gjettet

    else:
        antall_liv -=1
        print("Bokstaven er ikke i løsningsordet.")
        if antall_liv == 0:
            break
        else:
            print("Du har",antall_liv,"liv igjen.")


#Vise vinn/tap-melding
if antall_liv == 0:
    print("Du tapte, riktig svar var",'"'+str(hemmelig_ord)+'"')
else:
    print("Du har vunnet! Du hadde",antall_liv,"liv igjen.")
'''

hemmelig_ord = input("Skriv inn det hemmelige ordet\n:::")
print("\n:\n:\n:\n:\n:\n:\n:\n:\n:\n:\n:\n:\n:\n:\n:\n:\n:\n:\n:\n:\n:\n:\n:\n:\n:\n:\n:\n:\n:\n:\n:\n:\n:\n:\n:\n:\n:\n:\n:\n:\n")
antall_liv == int(input("Skriv inn antall liv\n:::"))

def skrivUtListe(liste):
    tekst = ''
    for i in liste:
        tekst += i
    print(tekst)
