import math
class Circulo:                  #clase
    def __init__(self, radio):    #
        self.radio=radio

    def area(self):             #metodo/funcionalidad
        area=(math.pi)*(self.radio**2)
        return area

c1=Circulo(10)
area=c1.area()
print(f"El area es {area}")