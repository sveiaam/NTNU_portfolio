#a, b, c)
k=int(input("Skriv inn det k antall iterasjoner (vil behandle k Fibonacci-tall) \n\n ::: "))
print("\n:-:-:-:-:-:-:-:-:-:-:-:-:-:-:\n")    #Estetisk
y=0

def fib(n):         #fib() returnerer Fibonacci-tall nr. n
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

for i in range(1,k+1):
    x = fib(i)      #lar x = Fibonacci-tall nr. i
    y += x          #lar y være summen av alle Fibonacci-tall nr. i
    print("ledd nr",i,"har verdi",x)        #Dette lager lista over tall

print("\nFibonacci-tall nr",k,"er",x,"\n")      #Dette printer det siste tallet.
print("Summen av de",k,"første Fibonacci-tall er",y,"\n")       #Dette printer summen

#k=antall ledd som skal summeres, x=verdien av ledd i
#y=summen av alle ledd x for en range av i, n=funksjonsparameter
