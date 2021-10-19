def numbers_liste():
    numbers = []
    for i in range(1,35):
        numbers.append(i)
    return numbers
def my_guess_liste():
    print("Du skal gjette 7 tall f.o.m. 1, t.o.m. 34. Ikke gjett samme tall flere ganger.\n")
    my_guess = []
    for i in range(7):
        tall = 0
        while (tall < 1) or (tall > 34) or (tall in my_guess):
            print("Tall nr,",i+1)
            tall = int(input("Hvilket tall gjetter du? (1-34)\n::: "))
        my_guess.append(tall)
    return my_guess
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

numbers = numbers_liste()   #Tall 1-34
my_guess = my_guess_liste() #7 tall gjettet av bruker i range 1-34

print("Din lottorekke er",sorted(my_guess),"\n")

trukkede_tall, trukkede_tilleggstall= trekk_tall(numbers)  #7 vinnertall, 3 tilleggstall

print("\nDe trukkede tallene er:",sorted(trukkede_tall),",tilleggstall er:",sorted(trukkede_tilleggstall),"\n")

antall_rette = compList(my_guess, trukkede_tall)    #Antall rette vinnertall
antall_rette_tillegg = compList(my_guess, trukkede_tilleggstall) #Antall rette tilleggstall

print("\nDu hadde",antall_rette,"riktige tall, og",antall_rette_tillegg,"antall riktige tilleggstall\n")

gevinst = premie(antall_rette, antall_rette_tillegg)     #Hvor stor premie brukeren får

print("Din premie er:",gevinst,",-")


'''
Gjennomsnittlig profitt ved 1 million rekker: -3 659 685, 1 kr,
etter 50 kjøringer av 1 million rekker.
Førstepremien ble vunnet 9 ganger av 50 millioner kjøringer..
'''
