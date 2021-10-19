#a)
N=int(input("Skriv inn en heltallsverdi for 'N' (iterasjoner av summeformelen)\n\n::: "))
y=0

for i in range(1, N+1):     #Tar range fra 1 for å unngå 0 i nevner.
    x=1/(i**2)      #Lar x være verdien til et ledd med indeks i
    y+=x        #Legger til verdien x for hver gang til en annen verdi, y.

print("Summen av",N,"iterasjoner av fomelen gir svaret",format(y,".4f"),"\n")

#b)
tol=eval(input("Skriv inn en verdi for 'tol' (toleransen for endring i x per iterasjon) \n\n::: "))
y=0
i=1
x=10

while x >= tol:
    x=1/(i**2)
    i+=1
    y+=x

print("Etter",i,"iterasjoner ble toleranseverdien",tol,"nådd, og summen av disse var",format(y,'.5f'),"\n")
