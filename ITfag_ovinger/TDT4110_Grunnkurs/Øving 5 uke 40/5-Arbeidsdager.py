#a)

#Returnerer om year er skuddår
def is_leap_year(year):  #Fra oppgave. Avgjør om et år er skuddår.
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False

#Returnerer en verdi 0-6 for den hvilken dag year begynner på
def weekday_newyear(year):
    if year < 1900:
        return "Skriv inn et årstall etter 1900"
    if year == 1900:
        return 0
    dager = 0
    for i in range(1900,year):
        if is_leap_year(i):
            dager += 2
        else:
            dager += 1
    ukedag = dager % 7
    return ukedag

#Returnerer streng av ukedagnavn fra verdiene 0-6
def ukedag(year):
    ukedag = weekday_newyear(year)
    if ukedag == 0:
        return 'mandag'
    elif ukedag == 1:
        return 'tirsdag'
    elif ukedag == 2:
        return 'onsdag'
    elif ukedag == 3:
        return 'torsdag'
    elif ukedag == 4:
        return 'fredag'
    elif ukedag == 5:
        return 'lørdag'
    else:
        return 'søndag'

#b)

#Returnerer om en dag (0-6) er en arbeidsdag
def is_workday(day):
    if day == 0 or day == 1 or day == 2 or day == 3 or day == 4:
        return True
    else:
        return False

#c)

#Returnerer hvor mange arbeidsdager som er i year.
def workdays_in_year(year):
    a = weekday_newyear(year)
    if is_workday(a):   #Året begynner (og slutter) på en arbeidsdag.
        if is_leap_year(year):      #Året er skuddår
            if weekday_newyear(year+1) == 0 or weekday_newyear(year+1) == 6:
                return 261  #Den ekstra skuddårsdagen er lørdag/søndag

            else:
                return 262  #Den ekstra skuddårsdagen er en arbeidsdag.

        else:
            return 261  #Året er ikke et skuddår

    else:   #Året begynner (og slutter) ikke på en arbeidsdag.
        if is_leap_year(year):  #Året er et skuddår
            if weekday_newyear(year+1) == 0 or weekday_newyear(year+1) == 6:
                return 260  #Den ekstra skuddårsdagen er en lørdag/søndag

            else:
                return 261  #Den ekstra skuddårsdagen er en arbeidsdag

        else:
            return 260  #Året er ikke et skuddår

year = int(input("Skriv inn et årstall\n:::"))

for i in range(1900, year+1):
    print(i,"begynner på en",ukedag(i),"og har",workdays_in_year(i),"arbeidsdager.")
