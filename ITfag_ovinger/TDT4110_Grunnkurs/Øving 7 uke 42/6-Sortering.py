def bubble_sort(liste):
    tick = 1    #Bruker tick for å vurdere om listen er sortert
    while tick != 0:
        tick = 0
        for i in range(len(liste)-1):
            if liste[i] <= liste[i+1]:
                pass    #Har med dette for å lage klare regler for like tall
            else:
                liste[i],liste[i+1] = liste[i+1],liste[i]
                tick += 1   #Hvis sortering gjøres er tick != 0, while-løkke gjentas
    return liste

print(bubble_sort([9,3,1,5,0,2,4,8,6,7]))

def selection_sort(liste):
    sortert_liste = []
    while len(liste) > 0:
        a = max(liste)
        sortert_liste.insert(0, a)
        liste.pop(liste.index(a))
    return sortert_liste

print(selection_sort([9,3,1,5,0,2,4,8,6,7]))

