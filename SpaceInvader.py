from tkinter import *

fenetre = Tk()
fenetre.geometry("1200x900")
Label(fenetre, text = 'score').pack(padx = 20,pady = 0)
Button(fenetre, text = 'Nouvelle partie').pack(side = 'right' )
Button(fenetre, text = 'Quitter', command = fenetre.destroy).pack(side = 'right')

Canevas = Canvas(fenetre, width = 900, height = 700, bg = 'black')
Canevas.pack()
fenetre.mainloop()

Canevas.bind('<Space>', tir)

def tir():
    [xmin,ymin,xmax,ymax] = Canevas.coords(vaisseau)
    canevas.create_line(xmin, ymin + 1O, xmax, ymax + 10, width = 2, fill = 'blue'  , tag = 'tir')
    fenetre.after(200, actualisertir)

def actualisertir():
    Canevas.move('tir', 0, 10)
    Canevas.update()
    fenetre.after(200, actualisertir)