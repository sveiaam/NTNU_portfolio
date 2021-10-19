def fakultet(n):
    if n == 0:  return 1
    else:   return (n*fakultet(n-1))

def binomialkoeffesient(n,k):
    return fakultet(n)/(fakultet(k)*fakultet(n-k))

def pascal(n):
    for rad in range(n):
        liste = []
        for plass in range(rad+1):
            liste.append(int(binomialkoeffesient(rad, plass)))
        print(liste)

storrelse = int(input("Hvor mange rader i Pascaltrekanten? ::: "))
print()
pascal(storrelse)
print()

def polynomutvidelse(n):
    b = []
    p = []
    for plass in range(n+1):
        b.append(int(binomialkoeffesient(n, plass)))
    q = 0
    for koeffesient in b:
        p.append([koeffesient,'y^',n-q,"x^",q])
        q+=1
    for ting in p:
        print(ting)

storrelse_2 = int(input("(y+x)^n. n= ::: "))
print()
polynomutvidelse(storrelse_2)
