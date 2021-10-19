def main():
    logg("23:59", "Mr.Y", "Har du mottatt pakken?")
    logg("0:00", "Mdm. Evil", "Ja. Pakken er mottatt.")
    logg("0:03", "Dr. Horrible", "All you need is love!")
    logg("0:09", "Mr Y", "Dr. Horrible, Dr. Horrible , calling Dr. Horrible .")
    logg("0:09", "Mr. Y", "Dr. Horrible, Dr. Horrible wake up now.")
    logg("0:09", "Dr. Horrible", "Up now!")
        

def logg(tid, navn, melding):
    print("Klokken",tid,"sendte",navn,"følgende melding:",'"'+str(melding)+'"')

main()
