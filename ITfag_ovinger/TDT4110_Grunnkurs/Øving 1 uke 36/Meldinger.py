tid=str(input("Skriv et klokkeslett[hh:mm] her: "))
navn=input("Skriv et navn her: ")
melding=input("Skriv en melding her: ")

def logg(tid, navn, melding):
    print("Klokken",tid,"sendte",navn,"følgende melding:"'"'+str(melding)+'"'".")

logg(tid, navn, melding)
