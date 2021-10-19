def count_coins(coins):
    return sum(coins)

def num_coins(numbers):
    numcoins = []
    for i in numbers:
        numcoins_i = []
        tjuere = i//20
        numcoins_i.append(tjuere)
        i -= tjuere * 20
        tiere = i//10
        numcoins_i.append(tiere)
        i -= tiere * 10
        femmere = i//5
        numcoins_i.append(femmere)
        i -= femmere * 5
        enere = i//1
        numcoins_i.append(enere)
        i -= enere * 1
        numcoins.append(numcoins_i)
    return numcoins

def check_weight(list):
    vekt = [9.9, 6.8, 7.85, 4.35]
    return prikkprodukt(vekt, list)

#Fra vektoroppg.
def prikkprodukt(vec1, vec2):
    verdi = 0
    for i in range(len(vec1)):
        verdi += (vec1[i] * vec2[i])
    return verdi


def main():
    liste = [12,23,34,45,56,67,78,89,90,98,87,65,54,43,21]
    myntfordeling = num_coins(liste)
    vekt = check_weight(liste)
    print("Myntfordeling:",myntfordeling,"Vekt:",vekt,"g")

main()

