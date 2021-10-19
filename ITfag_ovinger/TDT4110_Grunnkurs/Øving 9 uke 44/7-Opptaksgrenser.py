def read_from_file(filename):   #Returnerer dictionary med k=navn, v=opptakspoeng.
    liste = []
    dictionary = {}
    f = open(filename, 'r')
    for linje in f.readlines():
        liste.append(linje.strip())
    f.close()
    for element in liste:
        liste[liste.index(element)] = list(element.split(','))
    for element in liste:
        dictionary[element[0]] = element[1]
    return dictionary

def alle_sokere(dictionary):
    counter = 0
    for value in dictionary.values():
        if value == '"Alle"':
            counter += 1
    return counter

def snitt_opptak_NTNU(dictionary):
    total = 0
    counter = 0
    for key, value in dictionary.items():
        #if key.startswith('"NTNU') and value != '"Alle"':  #Alternativt
        if (key[:5]== '"NTNU') and (value != '"Alle"'):
            total += float(value)
            counter += 1
    average = total/counter
    return average

def lavest_opptak(dictionary):
    lavest = 100
    studie = ''
    for key, value in dictionary.items():
        if (value != '"Alle"') and (float(value) < lavest):
            lavest = float(value)
            studie = key
    return studie

def print_fint(dictionary):
    for k,v in dictionary.items():
        print(k, ":::", v)

data = read_from_file('poenggrenser_2011.csv')
print_fint(data)
print("\n::::::::::::\n")
print(alle_sokere(data),"studieprogram slapp inn alle søkere.")
print("Gjennomsnittlig opptakskrav på NTNU:",snitt_opptak_NTNU(data),"poeng.")
print("Lavest opptakskrav: ",lavest_opptak(data))

