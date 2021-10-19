poeng=float(input("Skriv inn poengsum: "))  #Må ta inn float her for å dekke alle muligheter for feilmelding.
karakter="X"    #Setter karakter som en global variabel

if (poeng)%1 == 0:      #Teste om dette er et heltall (int)
    if poeng<0:
        print("\nFeil:\n\nIkke skriv inn negative tall\n")
    else:
        if 0<=poeng<=40:    #Poengskala
            karakter="F"
        elif poeng<=52:
            karakter="E"
        elif poeng<=64:
            karakter="D"
        elif poeng<=76:
            karakter="C"
        elif poeng<=88:
            karakter="B"
        else:
            karakter="A"

        print("\nKarakter: ", karakter)
else:
    print("\nFeil:\n\nSkriv inn et heltall\n")


