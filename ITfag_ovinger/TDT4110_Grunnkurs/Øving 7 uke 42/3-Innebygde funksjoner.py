def random_numbers_gen():
    liste = []
    import random
    for i in range(100):
        liste.append(random.randint(0,9))
    return liste
random_numbers = random_numbers_gen()

def finn_toere(liste):
    return liste.count(2)

def sum_av_liste(liste):
    return sum(liste)

def sorter_stigende(liste):
    return sorted(liste)

def typetall(liste):
    hoyeste = 0
    typetall = []
    for i in range(10):
        a = liste.count(i)
        if a > hoyeste:
            hoyeste = a
            typetall = []
            typetall.append(i)
        elif a == hoyeste:
            typetall.append(i)
    return typetall, hoyeste

def baklengs(liste):
    return liste[::-1]

print("tilfeldige tall:",random_numbers)
print("\nantall toere:",finn_toere(random_numbers))
print("\nsum av liste:",sum_av_liste(random_numbers))
print("\nstigende rekkefølge:",sorter_stigende(random_numbers))
print("\ntypetall, antall av dette/disse:",typetall(random_numbers))
print("\nliste baklengs:",baklengs(random_numbers))
