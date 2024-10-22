from tools import generators
from tools import decorators
def pedir_turno():
    perfumeria_funcion = generators.generador_turnos('perfumeria')
    farmacia_funcion = generators.generador_turnos('farmacia')
    cosmeticos_funcion = generators.generador_turnos('cosmeticos')
    while True:
        try:
            print('Para que modulo quieres turno')
            print('1) Perfumeria')
            print('2) Farmacia')
            print('3) Cosmeticos')
            print('4) Salir')
            number = int(input('Dame un numero: '))
            if number <= 0 or number > 4:
                print("Elige una de las 4 opciones por favor")
            elif number == 4:
                break
            else:
                opciones = {1: 'perfumeria',
                            2: 'farmacia',
                            3: 'cosmeticos'}
                funciones = {1: perfumeria_funcion,
                            2: farmacia_funcion,
                            3: cosmeticos_funcion}
                turno = opciones.pop(number)
                decorar_turno_funcion = funciones.pop(number)
                next_function = next(decorar_turno_funcion)
                turno_decorado = decorators.decorar_turno(next_function)
                turno_decorado()
        except ValueError:
            print('Ese no es un numero')
        else:
            print(f'Ingresaste el numero {number}')
    print('Gracias')

print('Hola buenas tardes, seleccione el modulo que desea')
pedir_turno()
