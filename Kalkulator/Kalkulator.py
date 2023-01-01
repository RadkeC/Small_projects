import tkinter


# Functions for buttons in GUI
def P1():
    # Clear screen if last action was button '='
    if DZIALANIE == '=': PC()
    # Add digit to the end of insert number
    LICZBA[AKTUALNA] += '1'
    # Update screen
    ekran.delete(0, tkinter.END)
    ekran.insert(0, LICZBA[AKTUALNA])
    
    
def P2():
    # Clear screen if last action was button '='
    if DZIALANIE == '=': PC()
    # Add digit to the end of insert number
    LICZBA[AKTUALNA] += '2'
    # Update screen
    ekran.delete(0, tkinter.END)
    ekran.insert(0, LICZBA[AKTUALNA])
    
    
def P3():
    # Clear screen if last action was button '='
    if DZIALANIE == '=': PC()
    # Add digit to the end of insert number
    LICZBA[AKTUALNA] += '3'
    # Update screen
    ekran.delete(0, tkinter.END)
    ekran.insert(0, LICZBA[AKTUALNA])
    
    
def P4():
    # Clear screen if last action was button '='
    if DZIALANIE == '=': PC()
    # Add digit to the end of insert number
    LICZBA[AKTUALNA] += '4'
    # Update screen
    ekran.delete(0, tkinter.END)
    ekran.insert(0, LICZBA[AKTUALNA])
    
    
def P5():
    # Clear screen if last action was button '='
    if DZIALANIE == '=': PC()
    # Add digit to the end of insert number
    LICZBA[AKTUALNA] += '5'
    # Update screen
    ekran.delete(0, tkinter.END)
    ekran.insert(0, LICZBA[AKTUALNA])
    
    
def P6():
    # Clear screen if last action was button '='
    if DZIALANIE == '=': PC()
    # Add digit to the end of insert number
    LICZBA[AKTUALNA] += '6'
    # Update screen
    ekran.delete(0, tkinter.END)
    ekran.insert(0, LICZBA[AKTUALNA])
    
    
def P7():
    # Clear screen if last action was button '='
    if DZIALANIE == '=': PC()
    # Add digit to the end of insert number
    LICZBA[AKTUALNA] += '7'
    # Update screen
    ekran.delete(0, tkinter.END)
    ekran.insert(0, LICZBA[AKTUALNA])
    
    
def P8():
    # Clear screen if last action was button '='
    if DZIALANIE == '=': PC()
    # Add digit to the end of insert number
    LICZBA[AKTUALNA] += '8'
    # Update screen
    ekran.delete(0, tkinter.END)
    ekran.insert(0, LICZBA[AKTUALNA])
    
    
def P9():
    # Clear screen if last action was button '='
    if DZIALANIE == '=': PC()
    # Add digit to the end of insert number
    LICZBA[AKTUALNA] += '9'
    # Update screen
    ekran.delete(0, tkinter.END)
    ekran.insert(0, LICZBA[AKTUALNA])
    
    
def P0():
    # Clear screen if last action was button '='
    if DZIALANIE == '=': PC()
    # Add digit to the end of insert number
    LICZBA[AKTUALNA] += '0'
    # Update screen
    ekran.delete(0, tkinter.END)
    ekran.insert(0, LICZBA[AKTUALNA])
   

# Adding button
def Pplus():
    global AKTUALNA, DZIALANIE
    AKTUALNA = 1
    DZIALANIE = '+'
 

# Substract button
def Pminus():
    global AKTUALNA, DZIALANIE
    AKTUALNA = 1
    DZIALANIE = '-'
    
  
# Multiply button
def Pmnozenie():
    global AKTUALNA, DZIALANIE
    AKTUALNA = 1
    DZIALANIE = '*'
    
 
# Divide button
def Pdzielenie():
    global AKTUALNA, DZIALANIE
    AKTUALNA = 1
    DZIALANIE = '/'
    
   
# Clear screen function
def PC():
    global AKTUALNA, DZIALANIE
    AKTUALNA = 0
    DZIALANIE = ''
    LICZBA[0] = LICZBA[1] = ''
    ekran.delete(0, tkinter.END)
    
    
# '=' button function
def Prowna():
    global DZIALANIE
    wynik = ''
    # Make calculations
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
    # Move result to first variable
    LICZBA[0] = wynik
    LICZBA[1] = ''
    # Update screen
    ekran.delete(0, tkinter.END)
    ekran.insert(0, wynik)
    DZIALANIE = '='

    
# Function creating GUI
def Okno():
    # Create GUI
    root = tkinter.Tk(className='KARKURATOR')
    root.geometry('360x205')

    # Create title, background and buttons field
    tkinter.Label(root, text='KARKURATOR').grid(row=0, columnspan=4,padx=1,pady=1)
    ekran = tkinter.Entry(root, bg='white', width=50)
    ekran.grid(row=1, columnspan=4, padx=1, pady=1)
    klawiatura = tkinter.Label(root, bg = 'blue', width=50, height=10).grid(rowspan=4, columnspan=4, padx=1, pady=1)

    return root, ekran


# Buttons creating function
def Przyciski():
    P=[]
    for i in range(len(znaki)):
        P.append(tkinter.Button(root, text=znaki[i], width=10, bg='red', fg='white', command=FUN[i]))
        P[i].grid(row=2+int(i/4), column=i%4, padx=1, pady=1)

    return P


# Initial conditions
LICZBA = ['', '']
AKTUALNA = 0
DZIALANIE = ''
znaki = '789/456*123-0=C+'
FUN = [P7, P8, P9, Pdzielenie, P4, P5, P6, Pmnozenie, P1, P2, P3, Pminus, P0, Prowna, PC, Pplus]


if __name__ == '__main__':
    root, ekran = Okno()
    przyciski = Przyciski()

    # Start GUI
    root.mainloop()
