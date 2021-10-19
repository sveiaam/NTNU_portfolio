
def gcd(a,b):       #Euklids algoritme for største felles divisor
    while b != 0:
        gammel_b = b
        b = a%b
        a = gammel_b
    return a


def reduce_fraction(a,b):       #Returnerer a og b dividert med største felles divisor
    fellesfaktor = gcd(a,b)         #Da blir brøken forkortet maksimalt
    a_red = a/fellesfaktor
    b_red = b/fellesfaktor
    return a_red, b_red

print("\nSkriv inn en brøk som skal forkortes:\n")

tall_1 = int(input("Teller\n:::"))
tall_2 = int(input("Nevner\n:::"))

teller, nevner = reduce_fraction(tall_1,tall_2)
print("Den reduserte brøken er :::",int(teller),"/",int(nevner),":::")

input()
