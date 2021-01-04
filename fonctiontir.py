from tkinter import *
from random import randint
import math
import time


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



def tiralien(): 
    [xmin,ymin,xmax,ymax] = canevas.coords(alien)
    canevas.create_line( xmin + (xmax-xmin)/2, ymax, xmax - (xmax-xmin)/2 , ymax+25, width = 2, fill = 'red', tag='tira')
    fenetre.after(randint(5000,20000),tiralien)

def actualisertiralien():
    canevas.move('tira', 0, 10)
    canevas.update()
    fenetre.after(100, actualisertiralien)

def touchealien():
    for i in canevas.find_withtag('tira'):
        if canevas.coords(i)[3] == canevas.coords(ok.vaiss)[1] and canevas.coords(ok.vaiss)[0]<canevas.coords(i)[0]<canevas.coords(ok.vaiss)[2]:
            canevas.delete(i)
            vie.set(vie.get()-1)
    fenetre.after(1,touchealien)


def supptiralien():
    for i in canevas.find_withtag('tira'):
        if canevas.coords(i)[3] > 470:
            canevas.delete(i)
    fenetre.after(100,supptiralien)


class Vaisseau():
    def __init__(self,canvas):
        self.xmin=10
        self.ymin=hauteur - 50
        self.xmax=50
        self.ymax=hauteur - 10
        self.canevas=canvas
        self.vaiss=self.canevas.create_rectangle(self.xmin,self.ymin,self.xmax,self.ymax, outline= 'white', fill = 'blue')

    def tirvaisseau(self):
        [xmin,ymin,xmax,ymax] = canevas.coords(self.vaiss)
        canevas.create_line( xmin + (xmax-xmin)/2 ,ymin-25 , xmax - (xmax-xmin)/2 , ymin, width = 2, fill = 'blue', tag='tirv')
        

    def actualisertirvaisseau(self):
        canevas.move('tirv', 0, -10)
        canevas.update()
        fenetre.after(100, self.actualisertirvaisseau)


    def supptirvaisseau(self):
        for i in canevas.find_withtag('tirv'):
            if canevas.coords(i)[1] < 20:
                canevas.delete(i)
        fenetre.after(1000, self.supptirvaisseau)

    def touchevaisseau(self):
        for i in canevas.find_withtag('tirv'):
            if canevas.coords(i)[1] == canevas.coords(alien)[3] and canevas.coords(alien)[0]<canevas.coords(i)[0]<canevas.coords(alien)[2]:
                canevas.delete(alien)
                canevas.delete(i)
        fenetre.after(1, self.touchevaisseau)


def clavier(event):
    if event.keysym == 'space':
        ok.tirvaisseau()


fenetre = Tk()
    
fenetre.geometry("1200x900")
Label(fenetre, text = 'score').pack(padx = 20,pady = 0)




largeur=640
hauteur=480
canevas=Canvas(fenetre,width=largeur,height=hauteur,bg='black')
canevas.pack(padx=5,pady=5)

canevas.bind_all('<Key>', clavier)


vie=IntVar(value=3)
Label(fenetre, textvariable=vie).pack(side='right')
Label(fenetre, text='Nombre de vies restantes: ').pack(side='right')


Button(fenetre, text = 'Nouvelle partie').pack(side = 'left', )

ok=Vaisseau(canevas)
ok.actualisertirvaisseau()
ok.supptirvaisseau()
ok.touchevaisseau()

X0=10
Y0=10
X1=60
Y1=60
alien = canevas.create_rectangle(X0,Y0,X1,Y1, outline= 'white', fill = 'red')
DeplacementAvant()

fenetre.after(randint(2000,10000),tiralien)
actualisertiralien()
supptiralien()
touchealien()
fenetre.mainloop()





