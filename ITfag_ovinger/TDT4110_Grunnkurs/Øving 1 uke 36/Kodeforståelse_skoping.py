
x = 5
y = 8
def main ():
    x = 7
    y = 3
    print ("i main :", x, y)
    swap (x,y)
    print ("i main :", x, y)
    printglobals ()
    print ("i main :", x, y)
def swap (x, y):
    x,y = y,x # Python triks for å bytte om to variabler .
    print (" ---> i swap :", x, y)
def printglobals ():
    print (" ---> i printglobals :", x, y)
main ()

#Printer de lokale variablene 7 og 3

#Kjører funksjonen swap. Denne funksjonen har parametere x og y, og vil derfor hente de lokale variablene fra main.
    #Den endrer så disse lokale variablene slik at de har omvendt verdi, og printer dette.

#Printer de lokale variablene 7 og 3 (Variabelendringen fra swap er ikke overført)

#Kjører funksjonen printglobals, denne funksjonen henter ikke parameterene x og y fra main, så de bruker globale variabler.
    #Den printer så disse.

#Printer de lokale variablene 7 og 3

print("""Printer de lokale variablene 7 og 3

Kjører funksjonen swap. Denne funksjonen har parametere x og y, og vil derfor hente de lokale variablene fra main.
    Den endrer så disse lokale variablene slik at de har omvendt verdi, og printer dette.

Printer de lokale variablene 7 og 3 (Variabelendringen fra swap er ikke overført)

Kjører funksjonen printglobals, denne funksjonen henter ikke parameterene x og y fra main, så de bruker globale variabler.
    Den printer så disse.

Printer de lokale variablene 7 og 3""")
