import tkinter

def P1():
    if DZIALANIE == '=': PC()
    LICZBA[AKTUALNA] += '1'
    ekran.insert(-1, '1')
    ekran.delete(0, tkinter.END)
    ekran.insert(0, LICZBA[AKTUALNA])
def P2():
    if DZIALANIE == '=': PC()
    LICZBA[AKTUALNA] += '2'
    ekran.delete(0, tkinter.END)
    ekran.insert(0, LICZBA[AKTUALNA])
def P3():
    if DZIALANIE == '=': PC()
    LICZBA[AKTUALNA] += '3'
    ekran.delete(0, tkinter.END)
    ekran.insert(0, LICZBA[AKTUALNA])
def P4():
    if DZIALANIE == '=': PC()
    LICZBA[AKTUALNA] += '4'
    ekran.delete(0, tkinter.END)
    ekran.insert(0, LICZBA[AKTUALNA])
def P5():
    if DZIALANIE == '=': PC()
    LICZBA[AKTUALNA] += '5'
    ekran.delete(0, tkinter.END)
    ekran.insert(0, LICZBA[AKTUALNA])
def P6():
    if DZIALANIE == '=': PC()
    LICZBA[AKTUALNA] += '6'
    ekran.delete(0, tkinter.END)
    ekran.insert(0, LICZBA[AKTUALNA])
def P7():
    if DZIALANIE == '=': PC()
    LICZBA[AKTUALNA] += '7'
    ekran.delete(0, tkinter.END)
    ekran.insert(0, LICZBA[AKTUALNA])
def P8():
    if DZIALANIE == '=': PC()
    LICZBA[AKTUALNA] += '8'
    ekran.delete(0, tkinter.END)
    ekran.insert(0, LICZBA[AKTUALNA])
def P9():
    if DZIALANIE == '=': PC()
    LICZBA[AKTUALNA] += '9'
    ekran.delete(0, tkinter.END)
    ekran.insert(0, LICZBA[AKTUALNA])
def P0():
    if DZIALANIE == '=': PC()
    LICZBA[AKTUALNA] += '0'
    ekran.delete(0, tkinter.END)
    ekran.insert(0, LICZBA[AKTUALNA])
def Pplus():
    global AKTUALNA, DZIALANIE
    AKTUALNA = 1
    DZIALANIE = '+'
def Pminus():
    global AKTUALNA, DZIALANIE
    AKTUALNA = 1
    DZIALANIE = '-'
def Pmnozenie():
    global AKTUALNA, DZIALANIE
    AKTUALNA = 1
    DZIALANIE = '*'
def Pdzielenie():
    global AKTUALNA, DZIALANIE
    AKTUALNA = 1
    DZIALANIE = '/'
def PC():
    global AKTUALNA, DZIALANIE
    AKTUALNA = 0
    DZIALANIE = ''
    LICZBA[0] = LICZBA[1] = ''
    ekran.delete(0, tkinter.END)
def Prowna():
    global DZIALANIE
    wynik = ''
    if DZIALANIE == '+':
        wynik = str(int(LICZBA[0]) + int(LICZBA[1]))
    if DZIALANIE == '-':
        wynik = str(int(LICZBA[0]) - int(LICZBA[1]))
    if DZIALANIE == '*':
        wynik = str(int(LICZBA[0]) * int(LICZBA[1]))
    if DZIALANIE == '/':
        if int(LICZBA[0]) % int(LICZBA[1]) != 0:
            wynik = str(float(int(LICZBA[0]) / int(LICZBA[1])))
        else:
            wynik = str(int(int(LICZBA[0]) / int(LICZBA[1])))
    LICZBA[0] = wynik
    LICZBA[1] = ''
    ekran.delete(0, tkinter.END)
    ekran.insert(0, wynik)
    DZIALANIE = '='

def Okno():
    root = tkinter.Tk(className='KARKURATOR')
    root.geometry('360x205')

    tkinter.Label(root, text='KARKURATOR').grid(row=0, columnspan=4,padx=1,pady=1)
    ekran = tkinter.Entry(root, bg='white', width=50)
    ekran.grid(row=1, columnspan=4, padx=1, pady=1)
    klawiatura = tkinter.Label(root, bg = 'blue', width=50, height=10).grid(rowspan=4, columnspan=4, padx=1, pady=1)

    return root, ekran

def Przyciski():
    P=[]
    for i in range(len(znaki)):
        P.append(tkinter.Button(root, text=znaki[i], width=10, bg='red', fg='white', command=FUN[i]))
        P[i].grid(row=2+int(i/4), column=i%4, padx=1, pady=1)

    return P


LICZBA = ['', '']
AKTUALNA = 0
DZIALANIE = ''

znaki = '789/456*123-0=C+'
FUN = [P7, P8, P9, Pdzielenie, P4, P5, P6, Pmnozenie, P1, P2, P3, Pminus, P0, Prowna, PC, Pplus]

if __name__ == '__main__':
    root, ekran = Okno()
    przyciski = Przyciski()




    root.mainloop()