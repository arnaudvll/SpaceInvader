from tkinter import *
import math

def DeplacementAvant() :
    global alien,X0,Y0,X1,Y1,largeur,hauteur
    if Y1 >= hauteur-10:
        canevas.delete(alien)
        alien2 = canevas.create_rectangle(10,10,20,20, outline= 'white', fill = 'red')
    elif X1==largeur-10:
        fenetre.after(100,DeplacementArriere)
    else:
        X1+=5
        X0+=5

        canevas.coords(alien,X0,Y0,X1,Y1)
        fenetre.after(100,DeplacementAvant)

def DeplacementArriere() :
    global alien,X0,Y0,X1,Y1,largeur,hauteur
    if X0==10:
        Y0+=100
        Y1+=100
        fenetre.after(100,DeplacementAvant)
        
    else:
        X1-=5
        X0-=5

        canevas.coords(alien,X0,Y0,X1,Y1)
        fenetre.after(100,DeplacementArriere)

def tir():
    global ok
    [xmin,ymin,xmax,ymax] = canevas.coords(ok)
    canevas.create_line(xmin+50, ymin+20, xmax-50, ymax-20, width = 2, fill = 'blue', tag='tir')
    

def actualisertir():
    canevas.move('tir', 0, -10)
    canevas.update()
    fenetre.after(100, actualisertir)


def supptir():
    for i in canevas.find_withtag('tir'):
        if canevas.coords(i)[1] < 20:
            canevas.delete(i)
    fenetre.after(1000,supptir)

def touche():
    for i in canevas.find_withtag('tir'):
        if canevas.coords(i)[1] == canevas.coords(alien)[3] and canevas.coords(alien)[0]<canevas.coords(i)[0]<canevas.coords(alien)[2]:
            canevas.delete(alien)
            canevas.delete(i)
    fenetre.after(1,touche)

def clavier(event):
    if event.keysym == 'space':
        tir()

fenetre = Tk()
    
    
fenetre.geometry("1200x900")
Label(fenetre, text = 'score').pack(padx = 20,pady = 0)


largeur=640
hauteur=480
canevas=Canvas(fenetre,width=largeur,height=hauteur,bg='black')
canevas.pack(padx=5,pady=5)

canevas.bind_all('<Key>', clavier)


ok=canevas.create_rectangle(300,200,400,300, outline= 'white', fill = 'red')

Button(fenetre, text = 'Nouvelle partie').pack(side = 'left', )

X0=10
Y0=10
X1=60
Y1=60
alien = canevas.create_rectangle(X0,Y0,X1,Y1, outline= 'white', fill = 'red')
DeplacementAvant()

actualisertir()
supptir()
touche()
fenetre.mainloop()


