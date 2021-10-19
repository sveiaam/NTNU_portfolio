### Sudoku ###

import math

#readFromFile returnerer en liste som er utgangspunktet for brettet
def readFromFile(filename):
    f = open(filename, 'r')
    size = int(f.readline())    #Første linje angir størrelsen på brettet
    board = [[0 for i in range(size)]for i in range(size)]  #Lager et tomt brett på matriseform
    stringArray = []
    for line in f.readlines():
        stringArray.append(line.strip())
    for y in range(size):
        for x in range(size):
            board[y][x] = int(stringArray[y][x])
    f.close()
    return board

#TEMP printing av brett
def print_fint(liste):
    for i in liste:
        print(i)

#for print_sudoku - testing
def intersperse(lst, item):
    result = [item] * (len(lst) * 2 - 1)
    result[0::2] = lst
    return result

#Work in progress
def print_sudoku(board):
    front = ['']
    for i in range(len(board)):
        front.append(i)
    for linje in board:
        linje = intersperse(linje, '|')
        linje.insert(0, '|')
        linje.insert(0, board.index(linje))
    print_fint(board)

#get_horizontal_list gir en liste over tall i raden til (x,y)
def get_horizontal_list(x,y,boardInfo):   #Generell
    return boardInfo[y]

#get_vertical_list gir en liste over tall i kolonnen til (x,y)
def get_vertical_list(x,y,boardInfo): #Generell
    liste = []
    for linje in boardInfo:
        liste.append(linje[x])
    return liste

#get_square_list gir en liste over tall i kvadratet til (x,y)
def get_square_list(x,y,boardInfo):
    partisjon = int(math.sqrt(len(boardInfo))) #gir partisjon 3 ved 9x9, 2 ved 4x4, etc.
    outlist = []
    xSquare = x//partisjon
    ySquare = y//partisjon
    for i in range(partisjon):
        for j in range(partisjon):
            outlist.append(boardInfo[partisjon*ySquare+i][partisjon*xSquare+j])
    return outlist

#get_conflict_numbers gir en liste over tall som ikke kan settes inn i (x,y)
def get_conflict_numbers(x,y,boardInfo):
    konflikttall = set()
    konflikttall.update(get_horizontal_list(x,y,boardInfo))
    konflikttall.update(get_vertical_list(x,y,boardInfo))
    konflikttall.update(get_square_list(x,y,boardInfo))
    return list(konflikttall.difference([0]))

#checkMove returnerer True om et trekk er gyldig, False ellers
def checkMove(number, x, y, boardInfo):
    if (0 <= number <= len(boardInfo)): #Sjekker om tallet er innenfor brettets størrelse
        if number in get_conflict_numbers(x,y, boardInfo): #Sjekker om tallet er i liste over tall som ikke kan settes inn
            return False
        else:   return True
    else:   return False

#bruker_input returnerer en liste med [x, y, tall] som bruker skrev inn.
def bruker_input():
    while True:
        gyldighet = 1
        input_data = str(input("Skriv inn et trekk (rad kolonne tall): "))
        liste = list(input_data.split(' '))
        for element in liste:
            if element.isdigit():
                liste[liste.index(element)] = int(element)
            else:   gyldighet = 0
        if len(liste) != 3:
            gyldighet = 0
        if gyldighet:
            break
    liste[0], liste[1] = liste[1], liste[0] #Bestemte meg for å ha input som rad:kolonne
    return liste

#avgjor_gyldighet returnerer True hvis trekket er gyldig, False ellers
def avgjor_gyldighet(trekk, boardInfo, originalBoard):
    x = trekk[0]
    y = trekk[1]
    tall = trekk[2]
    conflict_numbers = get_conflict_numbers(x,y,boardInfo)
    if tall == 0:
        if originalBoard[y][x] == 0:
            return True
        else:
            return False
    if tall in conflict_numbers:
        return False
    else: return True

#avgjor seier returnerer True hvis brettet er fylt, False ellers
def avgjor_seier(boardInfo):
    for i in boardInfo:
        for j in i:
            if j == 0:
                return False
    return True

#gjennomfor_trekk tar inn et trekk og brettets tilstand, og returnerer brettets nye tilstand
def gjennomfor_trekk(trekk, boardInfo):
    x = trekk[0]
    y = trekk[1]
    tall = trekk[2]
    boardInfo[y][x] = tall
    return boardInfo



def main():
    originalBoard = readFromFile("sudoku.txt")
    boardInfo = originalBoard.copy()
    while not avgjor_seier(boardInfo):
        print_fint(boardInfo)
        print_fint(originalBoard) #originalBoard endres (??)
        trekk = bruker_input()
        if avgjor_gyldighet(trekk, boardInfo, originalBoard):
            boardInfo = gjennomfor_trekk(trekk, boardInfo) #Dette endrer originalBoard
        else:
            print("Ulovlig trekk")
    print("Du har vunnet")

main()

#tall = 0 gir ulovlig trekk - originalBoard endres som boardInfo
#tall større enn brettstørrelsen godtas å plasseres, uansett hva som er der fra før (som ikke er det samme tallet som plasserers)
