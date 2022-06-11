import math

class Punto:

    def __init__(self,coor_x,coor_y):
        self.coor_x=coor_x
        self.coor_y=coor_y
    
    def __str__(self):
        return "({},{})".format(self.coor_x,self.coor_y)
    
    def cuadrante(self):
        if self.coor_x > 0 and self.coor_y > 0:
            print("{} esta en el primer cuadrante".format(self))
        elif self.coor_x > 0 and self.coor_y < 0:
            print("{} esta en el cuarto cuadrante".format(self))
        elif self.coor_x < 0 and self.coor_y > 0:
            print("{} esta en el segundo cuadrante".format(self))
        elif self.coor_x < 0 and self.coor_y < 0:
            print("{} esta en el tercer cuadrante".format(self))
        elif self.coor_x == 0 and self.coor_y != 0:
            print("{} esta en el eje X".format(self))
        elif self.coor_x != 0 and self.coor_y == 0:
            print("{} esta en el eje Y".format(self))
        else:
            print("{} esta en el origen de coordendas".format(self))
        
    def vector(self, p):
        print("El vector entre {} y {} es ({},{})".format(self,p,
        p.coor_x-self.coor_x,p.coor_y-self.coor_y))

    def distancia(self,p):
        d=math.sqrt((p.coor_x-self.coor_x)**2+(p.coor_y-self.coor_y)**2)
        print("La distanca entre los puntos {} y {} es: {}".format(self,p,d))

A=Punto(2,3)
B=Punto(5,5)
C=Punto(-3,-1)
D=Punto(0,0)

A.cuadrante()
B.cuadrante()

A.vector(B)
B.vector(A)

A.distancia(B)
B.distancia(A)




    
    
