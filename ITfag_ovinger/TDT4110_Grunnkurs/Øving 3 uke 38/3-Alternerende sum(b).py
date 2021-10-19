n=int(input("Skriv inn en verdi for 'n': "))
k=int(input("Skriv inn maksimal verdi (k): "))
total=0
x=0
for i in range(0,n+1):
    if i%2!=0:
        total+=i**2     #Oddetall
        if total>k:     #Sjekker om totalmengde har oversteget grenseverdien k
            total-=i**2     #Hvis ja; trekk fra det siste leddet.
            x=1     #Setter x lik 1 for å vise senere at summen ble brutt.
            break   #bryter summen.
    else:
        total-=i**2 #Partall

if x==0:    #Sjekker tilstanden til x etter endt for-setning.
    print("Summen av tallserien er:",total,". Antallet ledd i denne summen er",n)
else:
    print("Summen av tallserien før den overstiger",k,"er",total,". Antallet ledd i denne summen er",i-1)
