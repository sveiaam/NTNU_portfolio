#a)
toleranse = float(input("Skriv inn en toleranseverdi, tol (en verdi mellom 0 og 1 anbefales)\n:::"))

def oppg_a(tol):
    count = 0
    prod = 1
    endring = 1
    while endring >= tol:
        count += 1
        prod = prod * (1+1/count**2)
        endring = prod - prod/(1+1/count**2)
    return prod, count

if toleranse >= 0:
    a,b = oppg_a(toleranse)
    print("Prodktet ble",format(a,'.2f'),"etter",b,"iterasjoner.")
else:
    print("Velg et positivt tall.")




'''

#b)

def oppg_b(tol, endring, count, prod):
    if endring >= tol:
        count += 1
        prod = prod * (1+1/count**2)
        endring = prod - prod/(1+1/count**2)
        oppg_b(tol, endring, count, prod)
    else:
        return prod, count

c,d = oppg_b(toleranse,1,0,1)
print("Prodktet ble",format(c,'.2f'),"etter",d,"iterasjoner.")

'''
