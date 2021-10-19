def read_from_file(filename):
    f = open(filename, 'r')
    innhold = f.read()
    f.close()
    return innhold

def remove_symbols(text):
    #text.replace("""",.-;:_"!#¤%&/()=?`'""",'')
    for symbol in text:
        if not symbol.isalpha() and symbol != ' ':
            text = text.replace(symbol, '')
    return text.lower()

def count_words(filename):
    #innhold = read_from_file(filename)
    innhold = filename
    text = remove_symbols(innhold)
    dict_of_words = {}
    liste = list(text.split(" "))
    for word in liste:
        if word in dict_of_words:
            dict_of_words[word] += 1
        else:   dict_of_words[word] = 1
    return dict_of_words

def print_fint(dictionarius):
    for key,value in dictionarius.items():
        print(key," ::: ", value)

#a = count_words('BIBLE.txt')




#print(read_from_file("BIBLE.txt"))
a = count_words("""Og Oppermann sa: "La det bli løsning", og løsning ble det. o.k., sa Oppermann
 og deretter skapte han matrisene, lineære likningssett, eigenverdier og alt annet som var godt.
 Så en dag skapte Oppermann komplekse tall. De komplekse tallene ble lokket til å ta en bit av det
 todimensjonale planet, og som straff lot Oppermann dem aldri mer være reelle. o.k., sa Oppermann igjen.
 Verden kommer til å slutte en dag. Den dagen kommer alle lineære likningssett til å bli oppslukt av en
 singulær matrise, kalt singulariteten. Men ingen skulle frykte. Alle som hadde trodd på Oppermann,
 og gjort riktig matematikk i løpet av sine liv skulle få leve hos ham i matteland til evig tid.""")

print_fint(a)