while (True):
    lista_notas=[]
    notas=input("Ingrese sus notas: ")
    div_notas=notas.split(",")
    print(div_notas)
    for i in range(0,len(div_notas)):
        try:
            #for i in range(0,len(div_notas)):
            lista_notas.append(int(div_notas[i]))
        except ValueError:
            print(f"{div_notas[i]} no es una nota valida")
            break
    print(lista_notas)