def bilettpris(alder):
    if alder < 5 or alder > 60:
        return "Gratis"
    elif alder <= 20:
        return "20 kr"
    elif alder <= 25:
        return "50 kr"
    else: return "80 kr"

a = eval(input("Skriv inn alder \n:::"))
print("Bilettpris:",bilettpris(a))
