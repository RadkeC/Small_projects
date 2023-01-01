# Initial conditions
litery = 'ABCDEFGHIJKLMNOPRSTUWXYZ '
znak = '#'
przerwa = ' '
szerokosc = 5

#     A    B   C   D   E   F   G   H  I  J   K   L   M   N   O   P   R   S   T   U   W   X   Y   Z  ' '
l1 = [14, 30, 15, 30, 31, 31, 14, 17, 4, 30,  9, 16, 17, 17, 14, 28, 28, 15, 31, 17, 17, 17, 17, 31, 0]
l2 = [17, 17, 16, 17, 16, 16, 16, 17, 4, 2,  10, 16, 27, 25, 17, 18, 18, 16,  4, 17, 17, 10, 10,  2, 0]
l3 = [31, 30, 16, 17, 30, 30, 22, 31, 4, 2,  12, 16, 21, 21, 17, 28, 28, 14,  4, 17, 21,  4,  4,  4, 0]
l4 = [17, 17, 16, 17, 16, 16, 17, 17, 4, 18, 10, 16, 17, 19, 17, 16, 20,  1,  4, 17, 27, 10,  4,  8, 0]
l5 = [17, 30, 15, 30, 31, 16, 14, 17, 4, 12,  9, 30, 17, 17, 14, 16, 18, 30,  4, 14, 17, 17,  4, 31, 0]
l = [l1, l2, l3, l4, l5]


# Functions changing chars in text for positions in list
def decifer(tekst):
    pozycje = []
    for i in tekst:
        pozycje.append(litery.find(i))
    return pozycje


# Function changing binar form of letters into combination of signs and spaces
def przeksztalcenie(binar):
    odp = ''
    for i in range(2, len(binar)):
        if binar[i] == '1':
            odp += znak
        else:
            odp += przerwa
    for i in range(5 - len(odp)):
        odp = przerwa + odp
    return odp


# Function to print text in prompt line after line
def wyswietlanie(pozycje):
    for n in range(5):
        tekst = ''
        for i in pozycje:
            tekst += przeksztalcenie(bin(l[n][i])) + ' '
        print(tekst)

while True:
    erro = False
    txt = input('Wpisz tekst :').upper()
    for sign in txt:
        if sign not in litery:
            print('Nieakceptowany znak')
            erro = True

    if not erro: wyswietlanie(decifer(txt))
