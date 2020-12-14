from tkinter import *
 
class Alien ():
    def __init__ (self,x,y,canvas):
        self.x=x
        self.y=y
        self.canvas=canvas
        self.id=self.canvas.create_rectangle(x,y,x+10,y+10)
    def move(self):
        self.canvas.move(self.id,10,0)

    def GetCoords (self):
        return(self.x,self.y)
 
class Game():
    def __init__(self):
        self.largeur=640
        self.hauteur=480
        self.canvas=Canvas(fenetre,width=self.largeur,height=self.hauteur,bg='black').pack(padx=5,pady=5)
        self.aliens=[]
        self.bouton = Button(fenetre, text = 'Nouvelle partie',command =self.start_game).pack(side = 'right' )
    def start_game(self):
        self.aliens=self.create_aliens()
        self.move_aliens()
        
    def create_aliens(self):
        self.aliens.append(Alien(10,10,self.canvas))
        
    def move_aliens(self):
        for alien in self.aliens :
            alien.move()
        canvas.after(10,move_aliens)
        
fenetre = Tk()
fenetre.geometry("1200x900")        
Game()


fenetre.mainloop()        
        
    
'''def DeplacementAvant() :
    global alien,X0,Y0,X1,y1,largeur,hauteur
    if y1 >= hauteur-10:
        canevas.delete(alien)
        alien2 = canevas.create_rectangle(10,10,20,20, outline= 'white', fill = 'red')
    elif x1==largeur-10:
        fenetre.after(10,DeplacementArriere)
    else:
        x1+=5
        x0+=5

        canevas.coords(alien,X0,Y0,X1,Y1)
        fenetre.after(10,DeplacementAvant)

def DeplacementArriere() :
    global alien,X0,Y0,X1,Y1,largeur,hauteur
    if x0==10:
        y0+=100
        y1+=100
        fenetre.after(10,DeplacementAvant)
        
    else:
        x1-=5
        x0-=5

        canevas.coords(alien,X0,Y0,X1,Y1)
        fenetre.after(10,DeplacementArriere)'''


