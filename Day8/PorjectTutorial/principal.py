import numeros

def preguntar():
    print('Bienvenido a farmacia Python')
    while True:
        print("[P] - Perfumeria\n[F] - Farmacia\n[C] - Cosmetica")
        try:
            mi_rubro = input('Elija su rubro:').upper()
            #If the value does not exist generates a ValueError
            ['P', 'F', 'C'].index(mi_rubro)
        except ValueError:
            print('Esa no es una opcion valida')
        else:
            break
    numeros.decorador(mi_rubro)

def inicio():
    while True:
        preguntar()
        try:
            otro_turno = input('Quieres sacar otro turno? [S][N]:').upper()
        except ValueError:
            print('Esa no es una opcion valida')
        else:
            if otro_turno == "N":
                print('Gracias por su visita')
                break
inicio()