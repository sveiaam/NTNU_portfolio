def brett(list):
    for i in range(len(list)):
        print('\t',i+1,end='')
    for x in range(len(list)):
        print('\n   ------------')
        print(x+1,'|',end='')
        for j in range(len(list[x])):
            print(list[x][j],'|',end='',sep='')
    print('\n   ------------\n')

def vinner(liste):
    if liste[0][0]==liste[1][0]==liste[2][0]!='   ':
        return True
    elif liste[0][1]==liste[1][1]==liste[2][1]!='   ':
        return True
    elif liste[0][2]==liste[1][2]==liste[2][2]!='   ':
        return True
    elif liste[0][0]==liste[0][1]==liste[0][2]!='   ':
        return True
    elif liste[1][0]==liste[1][1]==liste[1][2]!='   ':
        return True
    elif liste[2][0]==liste[2][1]==liste[2][2]!='   ':
        return True
    elif liste[0][0]==liste[1][1]==liste[2][2]!='   ':
        return True
    elif liste[0][2]==liste[1][1]==liste[2][0]!='   ':
        return True
    return False

def navn():
    s1=input('Hvem er spiller1?  ')
    s2=input('Hvem er spiller2?  ')
    return s1,s2


def riktig(liste,x,i,j,):
    koord=[0,1,2]
    if i in koord and j in koord:
        if (x=='X'or x=='O') and liste[i][j]=='   ':
            return True
    return False

def tictactoe():
    brikker=[['   ' for x in range(3)] for y in range(3)]
    spiller1,spiller2 = navn()
    brett(brikker)
    while not vinner(brikker):
        print(spiller1,' sitt trekk')
        x,i,j='X',1,5
        while not riktig(brikker,x,i,j):
            x,i,j=input('Angi tegn(X/O) og koordinater (tegn,rad,kolonne): ').split(',')
            x,i,j=x.upper(),int(i)-1,int(j)-1
            if riktig(brikker,x,i,j):
                brikker[i][j]=' '+x.upper()+' '
                break
            else:
                print('Det er et ugyldig trekk')
        print('\n')
        brett(brikker)
        if vinner(brikker):
            print(spiller1,'har seiret!!')
            break
        print('\n',spiller2, ' sitt trekk')
        l,m,n='O',1,5
        while not riktig(brikker,l,m,n):
            l,m,n = input('Angi tegn(X/O) og koordinater (tegn,rad,kolonne): ').split(',')
            l,m,n=l.upper(),int(m)-1,int(n)-1
            if riktig(brikker,l,m,n):
                brikker[m][n]=' '+l.upper()+' '
                break
            else:
                print('Det er et ugyldig trekk')
        print('\n')
        brett(brikker)
        if vinner(brikker):
            print(spiller2,'har seiret!!')
            break


tictactoe()