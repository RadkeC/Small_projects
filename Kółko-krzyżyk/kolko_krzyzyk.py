import tkinter as tk
from PIL import Image, ImageTk

# Check if player (q) have 3 signs in row
def sprawdz(q, wynik):
    for i in range(3):
        # Vertical check
        if wynik[0+i] == wynik[3+i] == wynik[6+i] == q:
            return True
        # Horizontal check
        elif wynik[0+i*3] == wynik[1+i*3] == wynik[2+i*3] == q:
            return True
    # Cross check
    if wynik[0] == wynik[4] == wynik[8] == q:
        return True
    if wynik[2] == wynik[4] == wynik[6] == q:
        return True
    return False

# Function for game button to set field with player sign
def klikniecie(i):
    def f():
        # Check if field is untaken
        if wynik[i] == ' ':
            # Player X turn option
            if aktual[0] == 'x':
                # Set field image to players sign
                znacznik_tury.config(image=om)
                P[i].config(image = x)
                # Save change in table
                wynik[i] = 'x'
            # Player Y turn option
            else:
                # Set field image to players sign
                znacznik_tury.config(image=xm)
                P[i].config(image=o)
                # Save change in table
                wynik[i] = 'o'
            # Check if player won
            if sprawdz(aktual[0], wynik):
                # Set winning information
                odpowiedz.config(text="Gratulacje! Wygrał {}".format(aktual[0]))
                # Clear table (fields still are uncleard)
                for n in range(9): wynik[n] = ''
                # Show new game button
                znacznik_tury.config(image=odswiez)
            # Check if all fields are taken but noone won
            if ' ' not in wynik: znacznik_tury.config(image=odswiez)
            # Change actual player
            aktual.reverse()
    return f

# Function to clear game fields
def odsw(event):
    if znacznik_tury['image'] == 'odswiez':
        for n in range(9):
            wynik[n] = ' '
            P[n].config(image=pusty)
            odpowiedz.config(text="")
            if aktual[0] == 'x':
                znacznik_tury.config(image=xm)
            else:
                znacznik_tury.config(image=om)

                
# Set starting conditions
aktual = ['x', 'o']
wynik = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

# Create GUI
root = tk.Tk(className="ox")
root.geometry('480x600')

# Import images from files
xm = ImageTk.PhotoImage(Image.open('x.bmp').resize((50,50),Image.ANTIALIAS), name='xm')
om = ImageTk.PhotoImage(Image.open('o.png').resize((50,50),Image.ANTIALIAS), name='om')
odswiez = ImageTk.PhotoImage(Image.open('odswiez.jfif').resize((50,50),Image.ANTIALIAS), name='odswiez')
x = ImageTk.PhotoImage(Image.open('x.bmp').resize((150,150),Image.ANTIALIAS), name='x')
o = ImageTk.PhotoImage(Image.open('o.png').resize((150,150),Image.ANTIALIAS), name='o')
pusty = ImageTk.PhotoImage(Image.open('pusty.bmp').resize((150,150),Image.ANTIALIAS), name='pusty')

# Create game fields in GUI
# Turn marker
tura = tk.Label(root, text='TURA :', anchor='w', font=20).grid(row=0, column=1)
znacznik_tury = tk.Label(root, image=xm, anchor='e', borderwidth=2)
znacznik_tury.grid(row=0, column=2)
znacznik_tury.bind('<Button-1>', odsw)

# Game result field
odpowiedz = tk.Label(root, bg='white', font=20, width=20)
odpowiedz.grid(row=5, columnspan=3)

# 9 empty game fileds
P = []
obraz = []
for i in range(9):
    P.append(tk.Button(root, image=pusty, command=klikniecie(i)))
    P[i].grid(row=int(1+i/3), column=i%3)

# Starat GUI
root.mainloop()






