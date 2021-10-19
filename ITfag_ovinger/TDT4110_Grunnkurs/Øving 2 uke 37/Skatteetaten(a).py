print("""INFO:
Dette programmet trenger å vite hvor stor del av boligen som er utleid.
Oppgi dette i prosent (%). 100 betyr hele boligen, 50 betyr halvparten, 20 er en mindre del, osv.
""")

prosent=float(input("Skriv inn hvor mange prosent som er utleid: "))


if 100>=prosent>=0:     #Sjekker om prosentsaten gir mening
    leie = float(input("Skriv inn leieinntekt: "))
    if (prosent > 50) and (leie >= 20000):
        print("Skattepliktig beløp er:", '"' + str(leie) + '"',"kr.")
    else:
        print("Ingen skatteplikt i dette tilfellet.")
else:
    print("Skriv inn en prosentverdi mellom 0 og 100")
