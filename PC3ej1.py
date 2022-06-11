while(True):
    numero=input("Ingrese la fraccion en formato x/y: ")
    div=numero.split("/")
    num=div[0]
    den=div[1]
    try:
        cociente=(int(num)*100)//int(den)
        if (0<cociente<1):
            print("E")
        elif (100>=cociente>99):
            print("F")
        elif (1<=cociente<=99):
            print(f"{cociente}%")  

    except ZeroDivisionError:
        print("No puede dividir entre 0")
        continue
    except ValueError:
        print("Ingrese numeros enteros")
        continue
   