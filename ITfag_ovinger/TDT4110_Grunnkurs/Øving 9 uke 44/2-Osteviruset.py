cheeses = {
'cheddar':
('A235-4', 'A236-1', 'A236-2', 'A236-3', 'A236-5', 'C31-1', 'C31-2'),
'mozarella':
('Q456-9', 'Q456-8', 'A234-5', 'Q457-1', 'Q457-2'),
'gombost':
('ZLAFS55-4', 'ZLAFS55-9', 'GOMBOS-7', 'A236-4'),
'geitost':
('SPAZ-1', 'SPAZ-3', 'EMACS45-0'),
'port salut':
('B15-1', 'B15-2', 'B15-3', 'B15-4', 'B16-1', 'B16-2', 'B16-4'),
'camembert':
('A243-1', 'A234-2', 'A234-3', 'A234-4', 'A235-1', 'A235-2', 'A235-3'),
'ridder':
('GOMBOS-4', 'B16-3'),
}

#Oppg a)
port_salut_places = cheeses['port salut']
print("Plassering av port salut: ",port_salut_places)


#Oppg b)
def ostevirus(infest_hyller):
    infected_cheeses = []
    for key,value in cheeses.items():
        for plass in value:
            for infest in infest_hyller:
                if plass.find(infest) == 0 and key not in infected_cheeses:
                    infected_cheeses.append(key)
            #if ((plass[:2:] in tresifret) or (plass[:3:] in firesifret)) and key not in infected_cheeses:
                #infected_cheeses.append(key)
    return infected_cheeses

infisert_ost = ostevirus(['B13','B14','B15','C31','A234','A235'])
print("Mulige infiserte oster: ",infisert_ost)

#Oppg c)
def ok_ost_type(infected_cheeses):
    ok_ost = []
    for key,value in cheeses.items():
        if key not in infected_cheeses:
            ok_ost.append(key)
    return ok_ost

def print_ok_ost(ok_ost):
    for key, value in cheeses.items():
        if key in ok_ost:
            for plassering in value:
                print(plassering, key)

ok_ost = ok_ost_type(infisert_ost)
print("\nBrukbare oster: \n")
print_ok_ost(ok_ost)
