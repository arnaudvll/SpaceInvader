
class Vaisseau():
    def __init__(self,canvas,hauteur):
        self.xmin=10
        self.ymin=hauteur - 50
        self.xmax=50
        self.ymax=hauteur - 10
        self.canevas=canvas
        self.vaiss=self.canevas.create_rectangle(self.xmin,self.ymin,self.xmax,self.ymax, outline= 'white', fill = 'blue')

    def tirvaisseau(self):
        [xmin,ymin,xmax,ymax] = canevas.coords(self.vaiss)
        canevas.create_line( xmin + (xmax-xmin)/2 ,ymin-25 , xmax - (xmax-xmin)/2 , ymin, width = 2, fill = 'blue', tag='tirv')
        