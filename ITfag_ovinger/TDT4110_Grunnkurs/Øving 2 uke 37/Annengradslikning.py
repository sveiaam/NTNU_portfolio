a=int(input("Skriv inn en verdi for a: "))
b=int(input("Skriv inn en verdi for b: "))
c=int(input("Skriv inn en verdi for c: "))

d=b**2-4*a*c
if d>0:
    print("Likningen har to reelle løsninger.")
elif d==0:
    print("Likningen har én reell løsning.")
else:
    print("Likningen har to imaginære løsninger.")
