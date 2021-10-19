def inputvektor(nummer):
    print("\nSkriv inn følgende for vektoren vec",nummer)
    print("::::::::::::::")
    x = eval(input("1. koordinat (x) til vektor\n::: "))
    y = eval(input("2. koordinat (y) til vektor\n::: "))
    z = eval(input("3. koordinat (z) til vektor\n::: "))
    return [x, y, z]

vec1 = inputvektor(1)
print(vec1)

def skalarmult(vektor, skalar):
    vektor2 = []
    for i in vektor:
        vektor2.append(i * skalar)
    return vektor2

skalar = eval(input("\nSkriv inn en skalar\n::: "))

vec2 = skalarmult(vec1, skalar)
print(vec2)

def lengde_vektor(vektor):
    import math
    lengde = 0
    for i in vektor:
        lengde += i**2
    lengde = math.sqrt(lengde)
    return lengde

print("\nLengde før:",lengde_vektor(vec1),". Lengde etter:",lengde_vektor(vec2))

def assimiler_lengde(vec1, vec2):
    if len(vec1) != len(vec2):
        while len(vec1) > len(vec2):
            vec2.append(0)
        while len(vec2) > len(vec1):
            vec1.append(0)
    return vec1, vec2

def prikkprodukt(vec1, vec2):
    vec1, vec2 = assimiler_lengde(vec1, vec2)
    verdi = 0
    for i in range(len(vec1)):
        verdi += (vec1[i] * vec2[i])
    return verdi

vec3 = inputvektor(3)

print("\nPrikkproduktet er:",prikkprodukt(vec1, vec3))
