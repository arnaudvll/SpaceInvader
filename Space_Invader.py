from tkinter import *  #importation de tkinter
from random import randint #importation de la fonction aléatoire
 
class Alien (): #la classe alien va nous permettre de gerer les aliens individuellement
    def __init__ (self,x,y,canvas):     
        self.x=x #coord x de l'alien
        self.y=y #coord y de l'alien
        self.canvas=canvas #importation du canvas
        self.id=self.canvas.create_image(self.x,self.y, image=image_alien) #creation de l'objet image de l'alien

    def move_avant(self): #fonction permettant de deplacer l'alien vers la droite
        self.canvas.move(self.id,5,0)
        self.x+=5 #on met à jour la coord x

    def move_arriere(self): #fonction permettant de deplacer l'alien vers la gauche
        self.canvas.move(self.id,-5,0)
        self.x-=5 #on met à jour la coord x

    def move_down(self): #fonction permettant de deplacer l'alien vers le bas
        self.canvas.move(self.id,0,20)
        self.y+=20 #on met à jour la coord y

    def tir(self): #fonction permettant de creer le tir de l'alien 
        X,Y=self.GetCoords()
        tir=self.canvas.create_line( X, Y+10, X, Y+30, width = 2, fill = 'red', tag='tira') #on lui donne le hashtag 'tira'

    def GetCoords (self): #fonction permettant de recuperer les coord de l'alien (inutile)
        return(self.x,self.y)

    def delete_alien (self): #fonction permettant de supprimer l'alien de la classe Alien
         self.canvas.delete(self.id) 
                
class Game(): #classe permettant de gérer la partie
    def __init__(self):
        self.largeur=640
        self.hauteur=480
        self.canvas=Canvas(fenetre,width=self.largeur,height=self.hauteur,bg='black') #creation de notre canvas
        self.canvas.pack(padx=5,pady=5)
        self.aliens=[] #liste de stockage des objets aliens
        self.bouton = Button(fenetre, text = 'Nouvelle partie',command =self.start_game) #en appuyant sur le bouton, on execute la fonction start_game
        self.bouton.pack(side = 'right' )
        self.image_vaisseau = PhotoImage(file ="img_vaiss.png")
        self.h_vaiss,self.l_vaiss=self.image_vaisseau.height(),self.image_vaisseau.width()
        self.vie=IntVar(value=3)
        self.variable=Label(fenetre, textvariable=self.vie)
        self.variable.pack(side='right')
        self.text = Label(fenetre, text='Nombre de vies restantes: ')
        self.fin = Label(fenetre, text='game over')
        self.win = Label(fenetre, text='victoire')
        self.text.pack(side='right')
        self.bloc=[] #liste de stockage des blocs
        self.vais='' #stockage de notre vaisseau

    def start_game(self): #fonction qui execute toutes les fonctions necessaire au jeu
        self.create_vaisseau() 
        self.create_aliens()
        self.deplacement_avant()
        self.tir_alien()
        self.supp_tir_vaisseau()
        self.canvas.bind_all('<Key>',self.deplacement)
        self.touche_alien()
        self.touche_vaisseau()
        self.bouton.pack_forget() #on unpack le bouton nouvelle partie pour eviter d'avoir deux parties lancées à la fois 
        self.game_over()   
        self.create_bloc()
        self.bloc_touche()
        self.victoire()
        

    def create_aliens(self): #fonction permettant de créer les objets aliens et de les stocker dans la liste 
        self.aliens.append(Alien(10,20,self.canvas))
        self.aliens.append(Alien(50,20,self.canvas))
        self.aliens.append(Alien(90,20,self.canvas))
        self.aliens.append(Alien(130,20,self.canvas))
        self.aliens.append(Alien(170,20,self.canvas))

    def create_vaisseau(self): #fonction qui créer le vaisseau
        self.vaiss=self.canvas.create_image(250,400, image=self.image_vaisseau)
        
    def game_over(self): #fonction qui verifie en continue que les vie ne sont pas à 0
        if self.vie.get() ==0: #si les vie sont a 0, on reinitialise tous les parametres
            self.canvas.delete(self.vaiss)
            self.aliens=[]
            self.supp_bloc()
            self.vais=''
            self.vie.set(3)
            self.fin.pack(side='left') #on affiche le bouton defaite
            self.bouton.pack(side='right') #on repack le bouton nouvelle partie pour recommencer
        fenetre.after(1,self.game_over)    
    
    def deplacement_avant(self): #foncton permettant de gere le deplacement des aliens vers la droite
        alienfin =self.aliens[-1] #on regarde l'alien le plus a droite 
        X,Y=alienfin.GetCoords()
        if X+10 >= self.largeur-10: #si il arrive au bord du canvas, 
            self.deplacement_arriere() #on lance la fonction deplacement arriere
        else:
            for alien in self.aliens : 
                alien.move_avant() #sinon, on fait avancer chaque alien vers la droite
            fenetre.after(50,self.deplacement_avant) #et on relance cette fonction
        
    def deplacement_arriere(self): #foncton permettant de gere le deplacement des aliens vers la gauche
        aliendebut =self.aliens[0] #on regarde l'alien le plus a gauche
        X,Y=aliendebut.GetCoords()
        if X <= 20: #si il arrive au bord gauche du canvas,
            for alien in self.aliens :
                alien.move_down() #on fait descendre les aliens d'une ligne
                X,Y=alien.GetCoords()
                if Y >= self.hauteur-10 : #si les aliens arrivent au bord inferieur du canvas,
                    alien.delete_alien() #on les supprime
            self.deplacement_avant() #et on les fait se deplacer vers la droite 
        else:
            for alien in self.aliens :
                alien.move_arriere() #sinon, on fait avancer chaque alien vers la gauche
            fenetre.after(50,self.deplacement_arriere) #et on relance cette fonction

    def create_bloc(self): #fonction permettant de créer les blocs
        x=50
        y=350
        y2=360
        for i in range(6):
            self.bloc.append(self.canvas.create_rectangle(x,y,x+50,y2,outline='white',fill='gray20'))
            x+=100
            i+=1
            
    def bloc_touche(self): #fonction permettant de détruire les blocs lorsqu'ils sont touchés par un tir alien
        for brick in self.bloc: #on parcours la liste de bloc
            [x1,y1,x2,y2]=self.canvas.coords(brick) #on récupere les coord du bloc
            for i in self.canvas.find_withtag('tira'): #on parcours l'ensemble des éléments avec le hashtag 'tira' (le tirs des aliens)          
                if i in self.canvas.find_overlapping(x1,y1,x2,y2): #on regarde si le tir est dans la zone du bloc
                    self.canvas.delete(i) #si c'est le cas, on supprime le tir
                    self.canvas.delete(brick) #on supprime le bloc du canvas
                    self.bloc.remove(brick) #on supprime le block de la liste
        fenetre.after(1,self.bloc_touche) #on boucle la fonction
            
    def tir_alien(self): #fonction permettant de generer les tirs aléatoires des aliens aléatoires
        n=len(self.aliens) #on recupere le nombre d'alien dans la liste
        numero=randint(0,n-1) #on choisit aléatoirement un numero parmis le nombre d'alien
        tir=randint(1000,5000) #on choisit aléatoirement un temps de latence
        self.aliens[numero].tir() #l'alien choisit tir
        fenetre.after(tir,self.tir_alien) #on recommence avec la latence
    
    def actualiser_tir_alien(self): #fonction permettant d'acualiser les tirs des aliens pour qu'ils parcourent le canvas vers le bas 
        self.canvas.move('tira', 0, 10)
        fenetre.after(100, self.actualiser_tir_alien)

    def touche_vaisseau(self): #fonction permettant de regarder si un tir du vaisseau touche un alien
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
    
    def victoire (self):
        if self.aliens == []:
            self.canvas.delete(self.vaiss)
            self.aliens=[]
            self.supp_bloc()
            self.vais=''
            self.vie.set(3)
            self.win.pack(side='left')
            self.bouton.pack(side='right')
        fenetre.after(1,self.victoire)    

    def supp_bloc(self):
        for brick in self.bloc :
            self.canvas.delete(brick)
            self.bloc.remove(brick) 

    
    

        
fenetre = Tk()
fenetre.geometry("1200x900")       
image_alien = PhotoImage(file ="img_alien.ppm")
h,l=image_alien.height(),image_alien.width()
        
jeu=Game()
jeu.actualiser_tir_alien()
jeu.actualiser_tir_vaisseau()

fenetre.mainloop()       