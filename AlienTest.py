from tkinter import *
 
class Alien ():
    def __init__ (self,x,y,canvas):
        self.x=x
        self.y=y
        self.canvas=canvas
        self.id=self.canvas.create_rectangle(self.x,self.y,self.x+10,self.y+10,outline= 'white', fill = 'red')
    def move_avant(self):
        self.canvas.move(self.id,10,0)
        self.x+=10
    def move_arriere(self):
        self.canvas.move(self.id,-10,0)
        self.x-=10
    def move_down(self):
        self.canvas.move(self.id,0,100)
        self.y+=100
    def Suppr(self):
        self.canvas.delete(self)

    def GetCoords (self):
        return(self.x,self.y)
 
class Game():
    def __init__(self):
        self.largeur=640
        self.hauteur=480
        self.canvas=Canvas(fenetre,width=self.largeur,height=self.hauteur,bg='black')
        self.canvas.pack(padx=5,pady=5)
        self.aliens=[]
        self.bouton = Button(fenetre, text = 'Nouvelle partie',command =self.start_game).pack(side = 'right' )
        
    def start_game(self):
        self.create_aliens()
        self.deplacement_avant()
        
    def create_aliens(self):
        self.aliens.append(Alien(10,10,self.canvas))
        self.aliens.append(Alien(30,10,self.canvas))
        self.aliens.append(Alien(50,10,self.canvas))
    
    def deplacement_avant(self):
        alienfin =self.aliens[-1]
        X,Y=alienfin.GetCoords()
        if X+10 >= self.largeur-10:
            self.deplacement_arriere()
        else:
            for alien in self.aliens :
                alien.move_avant()
            fenetre.after(10,self.deplacement_avant)
        
    
    def deplacement_arriere(self):
        aliendebut =self.aliens[0]
        X,Y=aliendebut.GetCoords()
        if X <= 10:
            for alien in self.aliens :
                alien.move_down()
                X,Y=alien.GetCoords()
                if Y >= self.hauteur-10 :
                    alien.Suppr()
            self.deplacement_avant()
        else:
            for alien in self.aliens :
                alien.move_arriere()
            fenetre.after(10,self.deplacement_arriere)

        
fenetre = Tk()
fenetre.geometry("1200x900")        
Game()


fenetre.mainloop()        
        
    
'''def DeplacementAvant() :
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


