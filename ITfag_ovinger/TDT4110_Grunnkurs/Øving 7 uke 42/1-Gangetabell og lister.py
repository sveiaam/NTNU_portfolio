def separate(numbers, threshold):
    mindre_enn_thres = []
    storre_enn_thres = []
    for i in numbers:
        if i < threshold:
            mindre_enn_thres.append(i)
        else: storre_enn_thres.append(i)
    return mindre_enn_thres, storre_enn_thres

liste1 = [1,2,3,4,5,6,7,8,9,10]
threshold = 5

def multiplication_table(n):
    liste1 = []
    for i in range(1,n+1):
        liste2 = []
        for j in range(1,n+1):
            liste2.append(i*j)
        liste1.append(liste2)
    return liste1

storrelse = int(input("Hvor stor gangetabell? \n::: "))
gangetabell = multiplication_table(storrelse)

import numpy as np
print(np.matrix(gangetabell))

