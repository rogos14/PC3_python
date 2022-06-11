#No entedi muy bien el enunciado :(
class Alumno:
    nombre="Pablo"
    registro="15437"
    
    def display(self):
        print(Alumno.nombre, Alumno.registro)

    def setAge(self):
        edad=input("Asignar edad al estudiante")
        return edad
    
    def setNota(self):
        nota=input("Asignar notas: ")
        return nota
    
alumno1=Alumno().nombre



