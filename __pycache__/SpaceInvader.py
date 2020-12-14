from tkinter import *


fenetre = Tk()
fenetre.geometry("1200x900")
Label(fenetre, text = 'score').pack(padx = 20,pady = 0)
Button(fenetre, text = 'Nouvelle partie').pack(side = "left" )
Button(fenetre, text = 'Quitter')

bg=Canvas (fenetre, width="1200",height="900" ,bg='blue')
bg.pack()
vesseau=bg.create_rectangle(580, 800,620,840,outline='red',fill='white' )
def deplacement(event):
    global vesseau
    global bg
    key=event.keysym
    print(key)
    xmin=bg.coords(vesseau)[0]
    xmax=bg.coords(vesseau)[2]
    if xmin>0 :
        if key=="Left":
            bg.move(vesseau, -20  , 0 )
        if key=="Right":
            bg.move(vesseau, 20  , 0 )
    if xmin<0 :
        if key=="Left":
            bg.move(vesseau, -20  , 0 )
        if key=="Right":
            bg.move(vesseau, 20  , 0 )


bg.focus_set()
bg.bind_all('<Key>',deplacement)


    
fenetre.mainloop()