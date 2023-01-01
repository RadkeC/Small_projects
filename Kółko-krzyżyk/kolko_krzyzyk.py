import tkinter as tk
from PIL import Image, ImageTk

def sprawdz(q, wynik):
    for i in range(3):
        if wynik[0+i] == wynik[3+i] == wynik[6+i] == q:
            return True
        elif wynik[0+i*3] == wynik[1+i*3] == wynik[2+i*3] == q:
            return True
    if wynik[0] == wynik[4] == wynik[8] == q:
        return True
    if wynik[2] == wynik[4] == wynik[6] == q:
        return True
    return False

def klikniecie(i):
    def f():
        if wynik[i] == ' ':
            if aktual[0] == 'x':
                znacznik_tury.config(image=om)
                P[i].config(image = x)
                wynik[i] = 'x'
            else:
                znacznik_tury.config(image=xm)
                P[i].config(image=o)
                wynik[i] = 'o'
            if sprawdz(aktual[0], wynik):
                odpowiedz.config(text="Gratulacje! Wygrał {}".format(aktual[0]))
                for n in range(9): wynik[n] = ''
                znacznik_tury.config(image=odswiez)
            if ' ' not in wynik: znacznik_tury.config(image=odswiez)
            aktual.reverse()
    return f

def odsw(event):
    print(znacznik_tury['image'])
    if znacznik_tury['image'] == 'odswiez':
        for n in range(9):
            wynik[n] = ' '
            P[n].config(image=pusty)
            odpowiedz.config(text="")
            if aktual[0] == 'x':
                znacznik_tury.config(image=xm)
            else:
                znacznik_tury.config(image=om)


aktual = ['x', 'o']
wynik = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

print(wynik)
root = tk.Tk(className="ox")
root.geometry('480x600')

xm = ImageTk.PhotoImage(Image.open('x.bmp').resize((50,50),Image.ANTIALIAS), name='xm')
om = ImageTk.PhotoImage(Image.open('o.png').resize((50,50),Image.ANTIALIAS), name='om')
odswiez = ImageTk.PhotoImage(Image.open('odswiez.jfif').resize((50,50),Image.ANTIALIAS), name='odswiez')
x = ImageTk.PhotoImage(Image.open('x.bmp').resize((150,150),Image.ANTIALIAS), name='x')
o = ImageTk.PhotoImage(Image.open('o.png').resize((150,150),Image.ANTIALIAS), name='o')
pusty = ImageTk.PhotoImage(Image.open('pusty.bmp').resize((150,150),Image.ANTIALIAS), name='pusty')


tura = tk.Label(root, text='TURA :', anchor='w', font=20).grid(row=0, column=1)
znacznik_tury = tk.Label(root, image=xm, anchor = 'e', borderwidth = 2)
znacznik_tury.grid(row=0, column=2)
znacznik_tury.bind('<Button-1>', odsw)

odpowiedz = tk.Label(root, bg='white', font = 20, width = 20)
odpowiedz.grid(row=5, columnspan = 3)

P = []
obraz = []
for i in range(9):
    P.append(tk.Button(root, image=pusty, command = klikniecie(i)))
    P[i].grid(row=int(1+i/3), column=i%3)




root.mainloop()






