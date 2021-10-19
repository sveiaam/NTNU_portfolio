import random
print('''Dette er et spill som handler om å
gjette et tall mellom 1 og n (rundt 1000 anbefales) på så få trekk som mulig
Hvis du gjetter nærmere enn 100 feil, får du beskjed
om at du var nære. Du får også vite om tallet er
høyere eller lavere enn det du gjettet.

Lykke til!
\n''')
topp=int(input("Skriv inn en heltallsverdi for øvre grense av gjetteleken: "))

tall1=random.randint(1,topp+1)
tall2=0
teller=0

while tall1 != tall2:
    tall2=int(input("Skriv inn et tall: "))
    teller += 1
    if tall1 == tall2:
        print("Tallene er like")
    else:
        print("Tallene er ulike")
        if tall2>tall1:
            if tall2>tall1+100:
                print("Tallet er mye lavere")
            else:
                print("Tallet er litt lavere")
        else:
            if tall2+100<tall1:
                print("Tallet er mye høyere")
            else:
                print("Tallet er litt høyere")
print("\n\nDu brukte",teller,"forsøk\n\n")

