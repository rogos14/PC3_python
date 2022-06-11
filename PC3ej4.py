class Rectangulo:
    def __init__(self,largo,ancho):
        self.largo=largo
        self.ancho=ancho
    
    def area(self):
        area=self.largo*self.ancho
        return area

r1=Rectangulo(10,5)
area=r1.area()
print(f"El area del rectangulo es {area}")
