#Oppg. a)
def randList(size, lower_bound, upper_bound):
    liste = []
    import random
    for i in range(size):
        liste.append(random.randint(lower_bound,upper_bound))
    return liste

#Oppg. b)
def compareLists(list1, list2):
    felles = []
    for i in list1:
        if i in list2 and i not in felles:  #Hvis 'i' finnes i 1 og i 2, og ikke er duplikat:
            felles.append(i)
    return felles

#Oppg. c)
def fjernDuplikater(liste):
    nyliste = []
    for i in liste:
        if i not in nyliste:
            nyliste.append(i)
    return nyliste
def multiCompList(lists):
    forenklet_lists = []
    felles = []
    for sublists in lists:  #Fjerner duplikater fra sublister
        forenklet_lists.append(fjernDuplikater(sublists))
    for i in lists[0]:  #Felles entry må også finnes i subliste #1.
        antall = 0  #Resetter antall sublister verdien 'i' finnes i.
        for sublists in lists:
            if i in sublists:
                antall += 1
        if antall >= len(lists):    #Hvis 'i' fantes i alle listene
            felles.append(i)
    return felles

#Oppg. d)
def longestEven(liste):
    counter = 0
    counter_max = 0
    indeks = 0
    for entry in liste:
        if entry %2 == 0 and counter == 0:  #Første partall etter en sekvens med odde
            indeks = liste.index(entry) #indeks til første tall lagres.
        if entry % 2 == 0:
            counter += 1    #Telleren økes ved partall.
        if entry %2 != 0:
            if counter == counter_max:
                max_indekser.append(indeks)
            elif counter > counter_max:
                max_indekser = []
                max_indekser.append(indeks)
                counter_max = counter
            counter = 0
    return max_indekser, counter_max


#main
def main():
    print(randList(10, 2, 7))
    a = [1, 2, 3]
    b = [4, 3, 1]
    print(compareLists(a, b))
    c = [7, 2, 1]
    d = [a, b, c]
    print(multiCompList(d))
    list = [4, 3, 3, 6, 2, 6, 8, 3, 4, 3, 3]
    print(longestEven(list))


main()
