from tkinter import *



fenetre = Tk()

fenetre.geometry("1200x900")

Label(fenetre, text = 'score').pack(padx = 20,pady = 0)

Button(fenetre, text = 'Nouvelle partie').pack(side = "left" )
Button(fenetre, text = 'Quitter')

image_vaisseau = PhotoImage(file ="img_vais.ppm")
bg=Canvas (fenetre, width="1920",height="1080" ,bg='black')


vaisseau=bg.create_image(250,800, anchor = NW, image=image_vaisseau )
bg.pack()
def deplacement(event):
    global vaisseau
    global bg
    key=event.keysym
    print(key)
    xmin=bg.coords(vaisseau)[0]

    print(xmin)
    if xmin>20 and xmin <1030:
        if key=="Left":
            bg.move(vaisseau, -35  , 0 )
        if key=="Right":
            bg.move(vaisseau, 35  , 0 )
    if xmin<=20 :
        if key=="Right":
            bg.move(vaisseau, 35  , 0 )
    if xmin >=1030:
        if key=="Left":
            bg.move(vaisseau, -35  , 0 )

bg.focus_set()
bg.bind_all('<Key>',deplacement)


    
fenetre.mainloop()

