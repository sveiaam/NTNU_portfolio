#y og x kalles variabler


###


x = 2
y = int(input ("Skriv inn et heltall: "))

z = x // y

#Feil: y bør spesifisere heltall: (y=int(input("Skriv inn et heltall"))
    #teksten i input er skrevet med blanding av ' og " dette må være konsekvent en av delene.
    #Kodebeskrivelsen sier ingenting om at koden skal printe dette tallet, så den delen bør fjernes.


###


a = 2
b = 3
if (b<(a) or (not b%a)):    #Sjekker om b er mindre enn a eller(or) om b er mindre enn ikke(not) b%a
                             #(altså større enn).
    b = a+b                 #b>a, (og b<b%a, men dette er ubetydelig for "eller"-kommandoen). Derfor kjøres "else"
else:
    a = a*b             #a=3*2=6
print("a: ",a)  #Printer a=6 og b=3
print("b: ",b)


###


def func1(a):
    import random   #importerer modulen "random"
    x = [0 for i in range(a)]   #Dette er en liste med kun én verdi

    for i in range(a):
        x[i] = random.randint(0, 10)    #x[i] er et tilfeldig tall f.o.m 0 t.o.m 10.

    return x    #Returnerer verdien til bruk i func2


def func2(x):
    return sorted(x)


# Dette er en kommentar
tall = int(input("Skriv inn et tall: "))
k = func1(tall)
y = func2(k)
print(y)

#Skriver inn et tall.
#func1 kjører med tallet som parameter. func1 genererer "tall" tilfeldige tall mellom 0 og 10, og returnerer disse som x
#func2 kjører med func1 som parameter, gir ut en liste med verdier sortert i stigende rekkefølge.
#programmet printer verdiene fra y.