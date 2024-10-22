from random import shuffle

# Lista inicial
palitos = ['-', '--', '---', '----']


#mezclar palitos
def mezclar(my_list):
    shuffle(my_list)
    return my_list


print(mezclar(palitos))


#pedir intento
def probar_suerte():
    intento = ''
    while intento not in ['1', '2', '3', '4']:
        intento = input("Elige un numero del 1 al 4: ")
    return int(intento)


#Comprobar intento
def chequear_intento(my_list, intento):
    if my_list[intento - 1] == '-':
        print("A lavar los platos")
    else:
        print("Esta vez te has salvado")
    print(f"Te ha tocado {my_list[intento - 1]}")


palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados, seleccion)