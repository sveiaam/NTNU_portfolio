def lille_gangetabell():
    for i in range(1,11):
        for j in range(1,11):
            if j == 1:
                print(" ============\n",i,"- gangen: \n")
            print(i*j)

lille_gangetabell()

print("\n\n===========================\n\n")

#Print primtall mellom 1 og 100:

'''
def er_primtall(tall):
        for i in range(2, tall):
            if (tall % i == 0):
                return False
            else:
                return True

for i in range(1, 101):
    a = er_primtall(i)
    if a is True:
        print(i,"er primtall")
'''

def er_primtall(n):
    if n > 1:
        for i in range(1,n):
            if n%i == 0:
                return False
        return True

for i in range(1,101):
    a = er_primtall(n)
    if n is true:
        print(i,"er primtall")