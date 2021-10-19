def allUnique(lst):
    if len(set(lst)) == len(lst):
        return True
    else: return False

print(allUnique([1,2,3,4,5]))


def removeDuplicates(liste):
    return list(set(liste))

print(removeDuplicates([1,2,5,4,2,1,3,4,5,6,6,4,1,2,3,1,5,2,3,4]))


def inAbutnotB(a,b):
    return sorted(list(set(a)-set(b)))
        #Bruker sorted fordi den gav en snål rekkefølge hvis ikke

print(inAbutnotB([1,2,3,4,5,6,7,8,9,10],[2,4,6,8,10]))


import numpy as np

def areOrthogonal(a,b):
    npa = np.array(a)
    npb = np.array(b)
    if np.dot(npa, npb) == 0:
        return True
    else: return False

print(areOrthogonal([1,0,0],[0,1,0]))


liste1 = np.array([1,2,3,4,5])
liste2 = np.array([6,7,8,9,10])
liste3 = np.array([11,12,13,14,15])
a = np.array([liste1, liste2, liste3])
b = np.transpose(a)

print(b)
