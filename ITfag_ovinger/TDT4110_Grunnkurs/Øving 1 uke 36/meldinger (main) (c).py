n=0 #Definerer en global variabel n for "antall meldinger"

def main():     #Kjører logg med visse parametere
    logg("23:59", "Mr.Y", "Har du mottatt pakken?")
    logg("0:00", "Mdm. Evil", "Ja. Pakken er mottatt.")
    logg("0:03", "Dr. Horrible", "All you need is love!")
    logg("0:09", "Mr Y", "Dr. Horrible, Dr. Horrible , calling Dr. Horrible .")
    logg("0:09", "Mr. Y", "Dr. Horrible, Dr. Horrible wake up now.")
    logg("0:09", "Dr. Horrible", "Up now!")
        

def logg(tid, navn, melding):
    global n
    n+=1    #Legger til 1 i den globale variabelen for hver gang logg calles.
    print("Msg",n,",",tid,":",navn,"sendte følgende melding:",'"'+str(melding)+'"')

main()
