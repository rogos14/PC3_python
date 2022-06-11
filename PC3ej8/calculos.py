import operaciones
try:
    operaciones.sumar(2,5)
    operaciones.restar(3,4)
    operaciones.producto(4,2)
    operaciones.dividir(3,6)
except TypeError:
    print("Tipo de dato no valido")
except NameError:
    print("Dato no valido")


