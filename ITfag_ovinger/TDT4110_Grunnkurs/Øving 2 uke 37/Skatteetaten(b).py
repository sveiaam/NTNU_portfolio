print("""INFO:
Dette programmet trenger å vite typen bolig som leies ut
som er forskjellig fra vanlig bolig).
Oppgi om boligen er en "Sekundærbolig" eller "Fritidsbolig"
""")

x=0

while x == 0:
    boligtype = str(input("\nSkriv inn boligtype (Sekundærbolig/Fritidsbolig) her: \n"))
    if boligtype == 'sekundærbolig' or boligtype == "Sekundærbolig" or boligtype == "sekundær" or boligtype == "Sekundær":
        x=1
        while x == 1:
            print("""\nDu har valgt "sekundærbolig".\nVennligst oppgi følgende:\n""")
            inntekt_sek = input("Skriv inn leieinntekten(pr år, pr bolig) her: ")
            antall_sek = input("Skriv inn hvor mange sekundærboliger du leier ut: ")
            if str.isdigit(inntekt_sek) == True and str.isdigit(antall_sek) == True:
                x=2
                inntekt_sek_float = float(inntekt_sek)
                antall_sek_float = float(antall_sek)
                print("Skattepliktig inntekt er",inntekt_sek_float*antall_sek_float,"kr.")
            else:
                print("Skriv inn gyldige verdier (tall)")

    elif boligtype == "fritidsbolig" or boligtype == "Fritidsbolig" or boligtype == "fritid" or boligtype == "Fritid":
        x=1
        print("""\nDu har valgt "fritidsbolig".

        INFO:
        Dersom du helt eller delvis bruker fritidsboligen til fritidsforemål,
        og selv bruker eiendommen i rimelig omfang over tid, kan du oppgi at
        boligen primært er til for fritidsforemål. Ellers oppgir du at den
        primært brukes for utleie. Oppgi også antallet boliger av denne typen
        som leies ut, og (midlere) utleieinntekt pr bolig pr år:\n""")

        while x == 1:
            formål=str(input("Skriv inn formålet med boligen(e) (Fritid/Utleie): \n"))

            if formål == "fritid" or formål == "Fritid" or formål == "fri" or formål == "Fri":
                x=2
                while x == 2:
                    print("""\nDu har valgt "fritid", vennligst oppgi følgende: \n""")
                    inntekt_fri = input("Skriv inn leieinntekten(pr år, pr bolig) her: \n")
                    antall_fri = input("Skriv inn antallet boliger av gjeldende type som leies ut: \n")
                    if str.isdigit(inntekt_fri) == True and str.isdigit(antall_fri) == True:
                        x=3
                        inntekt_fri_float = float(inntekt_fri)
                        antall_fri_float = float(antall_fri)
                        if inntekt_fri_float > 10000:
                            nettoskatt = (inntekt_fri_float - 10000) * 0.85
                            print("Skattepliktig beløp er:", nettoskatt * antall_fri_float)
                        else:
                            print("Inntekten er ikke skattepliktig.")
                    else:
                        print("Skriv inn gyldige verdier (tall)")

            elif formål == "utleie" or formål == "Utleie" or formål == "leie" or formål == "Leie":
                x=2
                while x == 2:
                    print(""""\nDu har valgt "utleie", vennligst oppgi følgende:\n""")
                    inntekt_fri = input("Skriv inn leieinntekten(pr år, pr bolig) her: \n")
                    antall_fri = input("Skriv inn antallet boliger av gjeldende type som leies ut: \n")
                    if str.isdigit(inntekt_fri) == True and str.isdigit(antall_fri) == True:
                        x=3
                        inntekt_fri_float = float(inntekt_fri)
                        antall_fri_float = float(antall_fri)
                        print("Skattepliktig beløp er:", inntekt_fri_float * antall_fri_float)
                    else:
                        print("Skriv inn gyldige verdier (tall)")
            else:
                print("""\nSkriv "Fritid" eller "Utleie"\n""")
    else:
        print("""\nSkriv inn "sekundærbolig" eller "fritidsbolig".\n""")
