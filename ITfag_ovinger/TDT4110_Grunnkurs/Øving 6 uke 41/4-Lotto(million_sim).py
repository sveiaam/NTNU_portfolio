def numbers_liste():
    numbers = []
    for i in range(1,35):
        numbers.append(i)
    return numbers
def my_guess_liste(numbers):
    import random
    trukkede_tall = []
    for i in range(7):
        a = random.choice(numbers)
        numbers.pop(numbers.index(a))
        trukkede_tall.append(a)
    return trukkede_tall
def trekk_tall(numbers):
    import random
    trukkede_tall = []
    trukkede_tilleggstall = []
    for i in range(7):
        a = random.choice(numbers)
        numbers.pop(numbers.index(a))
        trukkede_tall.append(a)
    for j in range(3):
        b = random.choice(numbers)
        numbers.pop(numbers.index(b))
        trukkede_tilleggstall.append(b)
    return trukkede_tall, trukkede_tilleggstall
def compList(gjettede_tall, trukkede_tall):
    antall_rette = 0
    for i in range(7):
        if gjettede_tall[i] in trukkede_tall:
            antall_rette += 1
    return antall_rette
def premie(like_tall, like_tilleggstall):
    if like_tall < 4:
        return 0
    if like_tall == 4 and like_tilleggstall >= 1:
        return 45
    if like_tall == 4:
        return 0
    if like_tall == 5:
        return 95
    if like_tall == 6 and like_tilleggstall >= 1:
        return 102110
    if like_tall == 6:
        return 3385
    if like_tall == 7:
        return 2749455
    else:   return 'Error'


def lotto_kjoring():
    numbers = numbers_liste()   #Tall 1-34
    my_guess = my_guess_liste(numbers) #7 tall gjettet av bruker i range 1-34
    numbers = numbers_liste()
    trukkede_tall, trukkede_tilleggstall= trekk_tall(numbers)  #7 vinnertall, 3 tilleggstall
    antall_rette = compList(my_guess, trukkede_tall)    #Antall rette vinnertall
    antall_rette_tillegg = compList(my_guess, trukkede_tilleggstall) #Antall rette tilleggstall
    gevinst = premie(antall_rette, antall_rette_tillegg)     #Hvor stor premie brukeren får
    return gevinst

def gjenta():
    total = 0
    for i in range(1000000):
        enkeltresultat = lotto_kjoring()
        total += enkeltresultat
    return total

def gjenta_2():
    return gjenta() - 5000000



def main():
    b = 0
    for i in range(50):
        a = gjenta_2()
        print("kjøring:",i,"| profitt:",a)
        b += a
    snitt = (b/50)
    print("\n\n:::",snitt,":::\n\n")

main()