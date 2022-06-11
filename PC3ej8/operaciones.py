
def sumar(a,b):
    suma=a+b
    print(f"La suma es: {suma}")
       
def restar(a,b):
    print(f"El resta es:{a-b}")

def producto(a,b):
    print(f"El producto es: {a*b}")

def dividir(a,b):
    try:
        cociente=a//b
        print(f"El cociente es: {cociente}")
    except ZeroDivisionError:
        print("No es posible dividir entre 0")


