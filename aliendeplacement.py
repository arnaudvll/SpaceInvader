from tkinter import *

def DeplacementAvant() :
    global alien,X0,Y0,X1,Y1,largeur,hauteur
    if Y1 >= hauteur-10:
        canevas.delete(alien)
        alien2 = canevas.create_rectangle(10,10,20,20, outline= 'white', fill = 'red')
    elif X1==largeur-10:
        fenetre.after(10,DeplacementArriere)
    else:
        X1+=5
        X0+=5

        canevas.coords(alien,X0,Y0,X1,Y1)
        fenetre.after(10,DeplacementAvant)

def DeplacementArriere() :
    global alien,X0,Y0,X1,Y1,largeur,hauteur
    if X0==10:
        Y0+=100
        Y1+=100
        fenetre.after(10,DeplacementAvant)
        
    else:
        X1-=5
        X0-=5

        canevas.coords(alien,X0,Y0,X1,Y1)
        fenetre.after(10,DeplacementArriere)


fenetre = Tk()
fenetre.geometry("1200x900")

Label(fenetre, text = 'score').pack(padx = 20,pady = 0)

largeur=640
hauteur=480
canevas=Canvas(fenetre,width=largeur,height=hauteur,bg='black')
canevas.pack(padx=5,pady=5)


X0=10
Y0=10
X1=60
Y1=60
alien = canevas.create_rectangle(X0,Y0,X1,Y1, outline= 'white', fill = 'red')
DeplacementAvant()

Button(fenetre, text = 'Nouvelle partie').pack(side = 'left', )
fenetre.mainloop()