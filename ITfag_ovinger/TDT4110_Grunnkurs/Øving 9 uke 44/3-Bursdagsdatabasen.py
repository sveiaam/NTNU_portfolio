birthdays = {
"22 nov": ["Lars", "Mathias"],
"10 des": " Elle ",
"30 okt": ["Veronica", "Rune"],
"12 jan": "Silje",
"31 okt": "Willy",
"8 jul": ["Brage", "Øystein"],
"1 mar": "Nina"
}

def add_birthday_to_date(date, name):
    try:
        birthdays[date].append(name)
    except AttributeError:  #Hvis AttributeError
        templiste = []  #Opprett liste
        templiste.append(birthdays[date])   #Legger til eksisterende verdi i liste
        templiste.append(name)  #Legger til ny verdi i liste
        birthdays[date] = templiste #Angir liste som value for key "date"
    except KeyError:    #Hvis KeyError
        birthdays[date] = name  #Oppretter en value for denne key


print(birthdays)
add_birthday_to_date("22 nov", "Petter")
print(birthdays)
add_birthday_to_date("12 jan", "Oppermann")
print(birthdays)
add_birthday_to_date("12 apr", "Svein")
print(birthdays)
add_birthday_to_date("12 apr", "Holger Fritz Von Schlaffenpaff")
print(birthdays)

