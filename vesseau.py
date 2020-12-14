from tkinter import *
def vesseau(fenetre,bg):

    vesseau=bg.create_rectangle(2, 4,3,5,fill="blue" ,outline="white")
    bg.focus_set()
    bg.bind('<key>',deplacement)
    
