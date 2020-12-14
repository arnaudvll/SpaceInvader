from tkinter import *
import math



def CreateAlien() :
    largeur =100
    hauteur=50
    canvas.create_rectangle(largeur,hauteur,10,10, outline= 'white', fill = 'red')
    



fenetre = Tk()
    
    
fenetre.geometry("1200x900")
Label(fenetre, text = 'score').pack(padx = 20,pady = 0)


canvas=Canvas(fenetre,width=640,height=480,bg='black')
canvas.pack(padx=5,pady=5)

Button(fenetre, text = 'Nouvelle partie',command=CreateAlien).pack(side = 'left', )
fenetre.mainloop()