def oppg_a():
    liste = []
    for i in range(100):
        liste.append(i)
    return liste

liste1 = oppg_a()   #Lager en liste med verdier 0-99
print(liste1)

def oppg_b(liste):
    total = 0
    for i in liste:
        if i%3 == 0 or i%10 == 0:
            total += liste[i]
    return total

oppgb = oppg_b(liste1)  #Summen av alle tall i lista delelige på 3 eller 10.
print(oppgb)

def oppg_c(liste):
    for i in liste:
        if liste[i]%2 == 0: #Partall
            liste[i] = liste[i]+1
        else:
            liste[i] = liste[i] -1
    return liste

liste2 = oppg_c(liste1) #Lista i (1) med tall parvis byttet plass
print(liste2)

def oppg_d(liste):
    return liste[::-1]

liste3 = oppg_d(liste2) #Den reverserte av lista i (3)
print(liste3)

'''
def oppg_d(liste):
    reversert = []
    while len(liste) > 0:
        siste_element = liste.pop(liste.index(liste[-1]))
        reversert.append(siste_element)
    return reversert
'''