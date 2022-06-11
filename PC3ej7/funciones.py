import random
def aleatorio(n:int):
    lista=[]
    for i in range(0,n):
        numero=random.randint(0,100)
        lista.append(numero)    
    return lista

def imprime(cadena):
    print(cadena)
    return

def ordenar(numeros):
    numeros.sort()
    print(numeros)
    
