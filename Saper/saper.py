from random import sample

def start():
    correct = False
    while not correct:
        try:
            m = input("Podaj rozmiar planszy (x,y) - max 26,26").split(',')
            x, y = int(m[0]), int(m[1])
            correct = not correct
        except:
            print('Nieprawidłowa forma danych')
    correct = False
    while not correct:
        try:
            n = int(input("Podaj liczbę min"))
            correct = not correct
        except:
            print('Nieprawidłowa forma danych')
    map, unhide_map = create_map(x, y, n)

    lose = False
    while not lose:
        print_map(x,y,unhide_map,n)
        if isWin(unhide_map, n):
            print('Wygrales')
            break
        target = input("Podaj pozycje bomby (+T dla postawienia flagi):")
        error, [xs, ys] = translate(target[0:2], x, y)

        if len(target) == 3 and target[2].upper() == 'T':
            if unhide_map[xs][ys] == 'T':
                unhide_map[xs][ys] = ' '
            elif unhide_map[xs][ys] == ' ':
                unhide_map[xs][ys] = 'T'
            continue
        if error or len(target)>2:
            continue
        lose, unhide_map = shoot(xs, ys, map, unhide_map)

    if lose: print('Przegrałeś!')


def translate(word, x, y):
    letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    error = False
    coordinates = [0, 0]
    c_list = list(word.upper())

    try:
        coordinates[0] = int(c_list[0])-1
        coordinates[1] = letters.index(c_list[1])
        error = False
    except:
        try:
            coordinates[0] = int(c_list[1])-1
            coordinates[1] = letters.index(c_list[0])
            error = False
        except:
            error = True
    if error:
        print('Złe wartości')

    if coordinates[0]>x-1 or coordinates[1]>y-1:
        print('Wartości spoza planszy')
        error = True
    return error, coordinates

def shoot(xs, ys, map, unhide_map):
    if map[xs][ys] == 'o':
        unhide_map[xs][ys] = 'X'
        lose = True
    else:
        count = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                try:
                    if map[xs+i][ys+j] == 'o' and xs+i>=0 and ys+j>=0:
                        count += 1
                except:
                    pass
        unhide_map[xs][ys] = count
        if count == 0:
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    try:
                        if xs + i >= 0 and ys + j >= 0 and unhide_map[xs+i][ys+j] == ' ':
                            lose,unhide_map = shoot(xs + i,ys + j,map,unhide_map)
                    except:
                        print('error', i,j)
        lose = False
    return lose, unhide_map

def print_map(x, y, unhide_map, n):
    letters=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    horizontal=letters[:y]
    vertical = list(range(0,x+1))
    vertical[0]=' '
    bombs_left= n-countT(unhide_map)

    for i in range(x+1):
        for j in range(y+1):
            if j == 0:
                if len(str(vertical[i])) == 1:
                    print(' ', end='')
                print(vertical[i], ' |', end=' ')
            elif i == 0:
                print(horizontal[j-1], ' |', end=' ')
            else:
                print(unhide_map[i-1][j-1], ' |', end=' ')
        print('')
    print('Pozostałe bomby: ', bombs_left)


def create_map(x, y, n):
    boombs_position = sample(range(x*y), n)
    map=[]
    unhide_map=[]
    for i in range(x):
        map.append([])
        unhide_map.append([])
        for j in range(y):
            unhide_map[i].append(' ')
            if i * y + j in boombs_position:
                map[i].append('o')
            else:
                map[i].append('x')
    return map, unhide_map

def isWin(unhide_map, n):
    number_of_left_poles = 0
    for i in range(len(unhide_map)):
        number_of_left_poles += unhide_map[i].count(' ')
        number_of_left_poles += unhide_map[i].count('T')
    if number_of_left_poles == n:
        return True
    else:
        return False

def countT(unhide_map):
    number_of_T=0
    for i in range(len(unhide_map)):
        number_of_T += unhide_map[i].count('T')
    return number_of_T

start()

