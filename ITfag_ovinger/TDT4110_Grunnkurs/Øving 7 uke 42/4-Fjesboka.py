def add_data(user):
    liste = user.split()
    ny_liste = []
    for i in liste:
        if str.isdigit(i):
            ny_liste.append(int(i))
        else:   ny_liste.append(i)
    return ny_liste

def get_person(given_name, facebook):
    sokeresultat = []
    for bruker in facebook:
        if bruker[0] == given_name:
            sokeresultat.append(bruker)
    return sokeresultat

facebook = [["Mark", "Zuckerberg", 32, "Male", "Married"],
                ["Therese", "Johaug", 28, "Female", "Complicated"],
                ["Mark", "Wahlberg", 45, "Male", "Married"],
                ["Siv", "Jensen", 47, "Female", "Single"]]

def main():
    print("Velkommen til facebook(tm).\n\n:::::::::::::::::::::::")
    nybruker = 'ikke done'
    while nybruker != 'done':
        print("\nLegg til en ny bruker. (Skriv 'done' for å avslutte).")
        nybruker = input("Skriv inn data (format: 'given_name surname age gender relationship_status')\n::: ")
        facebook.append(add_data(nybruker))
    facebook.pop(-1)  #'done' blir ikke tatt med i liste.
    sok = 'not_done'
    while sok != 'done':
        sok = input("\nSkriv inn ditt søk: ")
        resultat = get_person(sok,facebook)
        for profile in resultat:
            if profile[3] == 'Male' or profile[3] == 'male' or profile[3] == 'm':
                gender = 'his'
            else: gender = 'her'
            print(profile[0],profile[1],"is",profile[2],"years old,",gender,"relationship status is",profile[4])
    print("\n***\nLogger av facebook(tm)\n***\n")

main()