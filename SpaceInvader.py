from tkinter import *

fenetre = Tk()
fenetre.geometry("1200x900")
Label(fenetre, text = 'score').pack(padx = 20,pady = 0)
Button(fenetre, text = 'Nouvelle partie').pack(side = left, )
Button(fenetre, text = 'Quitter')
fenetre.mainloop()