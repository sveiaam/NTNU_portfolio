def isSixAtEdge(list):
    if (list[0] or list[-1]) == 6:
        return True
    else:   return False

def average(list):
    teller = sum(list)
    nevner = len(list)
    snitt = teller/nevner
    return snitt

def median(list):
    sortert = sorted(list)
    return sortert[int(len(sortert)/2)]


liste = [4,2,1,3,5]

print(isSixAtEdge(liste), average(liste), median(liste))

