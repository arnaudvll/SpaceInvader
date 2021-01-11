from tkinter import *
from random import randint
 
class Alien ():
    def __init__ (self,x,y,canvas):
        
        self.x=x
        self.y=y
        self.canvas=canvas
        self.id=self.canvas.create_image(self.x,self.y, image=image_alien)

    def move_avant(self):
        self.canvas.move(self.id,5,0)
        self.x+=5
    def move_arriere(self):
        self.canvas.move(self.id,-5,0)
        self.x-=5
    def move_down(self):
        self.canvas.move(self.id,0,20)
        self.y+=20
    def Suppr(self):
        self.canvas.delete(self)
    def tir(self):
        X,Y=self.GetCoords()
        tir=self.canvas.create_line( X, Y+10, X, Y+30, width = 2, fill = 'red', tag='tira')
    def GetCoords (self):
        return(self.x,self.y)
    def delete_alien (self):
         self.canvas.delete(self.id)
                
class Game():
    def __init__(self):
        self.largeur=640
        self.hauteur=480
        self.canvas=Canvas(fenetre,width=self.largeur,height=self.hauteur,bg='black')
        self.canvas.pack(padx=5,pady=5)
        self.aliens=[]
        self.bouton = Button(fenetre, text = 'Nouvelle partie',command =self.start_game)
        self.bouton.pack(side = 'right' )
        self.image_vaisseau = PhotoImage(file ="img_vaiss.png")
        self.vaiss=self.canvas.create_image(250,400, image=self.image_vaisseau)
        self.h_vaiss,self.l_vaiss=self.image_vaisseau.height(),self.image_vaisseau.width()
        self.vie=IntVar(value=3)
        self.variable=Label(fenetre, textvariable=self.vie)
        self.variable.pack(side='right')
        self.text = Label(fenetre, text='Nombre de vies restantes: ')
        self.fin = Label(fenetre, text='game over')
        self.text.pack(side='right')
        self.bloc=self.canvas.create_rectangle(200,250,200+30,260,outline='white',fill='gray20')
        
    def start_game(self):
        self.create_aliens()
        self.deplacement_avant()
        self.tir_alien()
        self.actualiser_tir_alien()
        self.actualiser_tir_vaisseau()
        self.supp_tir_vaisseau()
        self.canvas.bind_all('<Key>',self.deplacement)
        self.touche_alien()
        self.touche_vaisseau()
        self.bouton.pack_forget()
        self.game_over()
        self.bloc_touche()
        

    def create_aliens(self):
        self.aliens.append(Alien(10,20,self.canvas))
        self.aliens.append(Alien(50,20,self.canvas))
        self.aliens.append(Alien(90,20,self.canvas))
        self.aliens.append(Alien(130,20,self.canvas))
        self.aliens.append(Alien(170,20,self.canvas))
        
    def game_over(self):
        if self.vie.get() ==0:
            self.canvas.delete(self.vaiss)
            self.aliens=[]
            self.fin.pack(side='left')
            self.bouton.pack(side='right')
        fenetre.after(1,self.game_over)    
    
    def deplacement_avant(self):
        alienfin =self.aliens[-1]
        X,Y=alienfin.GetCoords()
        if X+10 >= self.largeur-10:
            self.deplacement_arriere()
        else:
            for alien in self.aliens :
                alien.move_avant()
            fenetre.after(50,self.deplacement_avant)
        
    def deplacement_arriere(self):
        aliendebut =self.aliens[0]
        X,Y=aliendebut.GetCoords()
        if X <= 20:
            for alien in self.aliens :
                alien.move_down()
                X,Y=alien.GetCoords()
                if Y >= self.hauteur-10 :
                    alien.Suppr()
            self.deplacement_avant()
        else:
            for alien in self.aliens :
                alien.move_arriere()
            fenetre.after(50,self.deplacement_arriere)
            
    def bloc_touche(self):   
        for i in self.canvas.find_withtag('tira'):
            for j in self.canvas.find_withtag('tirv'):
                life=2
                x_bloc=randint(15,610)
                
                [xmin_bloc,xmax_bloc,ymin_bloc,ymax_bloc]=self.canevas.coords(self.bloc)
                if (ymin_bloc == self.canvas.coords(i)[1] and xmin_bloc<=self.canvas.coords(i)[0]<=xmax_bloc) or (ymin_bloc == self.canvas.coords(j)[1] and xmin_bloc<=self.canvas.coords(j)[0]<=xmax_bloc):
                    life=life-1
                    self.canvas.delete(self.bloc)
                    if life == 1:
                        self.bloc=self.canevas.create_rectangle(x_bloc,250,x_bloc+30,260,outline='white',fill='gray50')
                    if life == 0:
                        self.bloc_touche()
        fenetre.after(1,bloc_touche)
            
    def tir_alien(self):
        n=len(self.aliens)
        numero=randint(0,n-1)
        tir=randint(1000,5000)
        self.aliens[numero].tir()
        fenetre.after(tir,self.tir_alien)
    
    def actualiser_tir_alien(self):
        self.canvas.move('tira', 0, 10)
        self.canvas.update()
        fenetre.after(100, self.actualiser_tir_alien)
        
    def touche_vaisseau(self):   
        for alien in self.aliens:
            x,y=alien.GetCoords()
            for i in self.canvas.find_withtag('tirv'):
                if i in self.canvas.find_overlapping(x,y,x+l,y+h):
                    self.aliens.remove(alien)
                    self.canvas.delete(i) 
                    alien.delete_alien()            
        fenetre.after(1, self.touche_vaisseau)
        
    
    def actualiser_tir_vaisseau(self):
        self.canvas.move('tirv', 0, -20)
        self.canvas.update()
        fenetre.after(100, self.actualiser_tir_vaisseau)


    def supp_tir_vaisseau(self):
        for i in self.canvas.find_withtag('tirv'):
            if self.canvas.coords(i)[1] < 20:
                self.canvas.delete(i)
        fenetre.after(1000, self.supp_tir_vaisseau)
        
    def touche_alien(self):    
        for i in self.canvas.find_withtag('tira'):
            x,y=self.canvas.coords(self.vaiss)[0],self.canvas.coords(self.vaiss)[1]
            if i in self.canvas.find_overlapping(x,y,x+self.l_vaiss,y+self.h_vaiss):
                self.canvas.delete(i)
                self.vie.set(self.vie.get()-1)
        fenetre.after(1,self.touche_alien)

    def deplacement(self,event):
        key=event.keysym
        x=self.canvas.coords(self.vaiss)[0]
        if key == 'space':
            [xmin,ymin] = self.canvas.coords(self.vaiss)
            self.canvas.create_line( xmin  , ymin-20, xmin  , ymin, width = 2, fill = 'blue', tag='tirv')
        if x>20 and x <580:
            if key=="Left":
                self.canvas.move(self.vaiss, -20 , 0)
            if key=="Right":
                self.canvas.move(self.vaiss, 20 , 0)
        if x<=20 :
            if key=="Right":
                self.canvas.move(self.vaiss, 20 , 0)
        if x >=580:
            if key=="Left":
                self.canvas.move(self.vaiss, -20 , 0)
    
    

        
fenetre = Tk()
fenetre.geometry("1200x900")       
image_alien = PhotoImage(file ="img_alien.ppm")
h,l=image_alien.height(),image_alien.width()
        
Game()


fenetre.mainloop()       