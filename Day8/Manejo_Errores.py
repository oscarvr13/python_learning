def suma():
    number1 = int(input('Dame el numero 1: '))
    number2 = int(input('Dame el numero 2: '))
    print(number1 + number2)
    print('Gracias por sumar' + number1)

try:
    suma()
#This catches the exception
except TypeError:
    print('Estas intentando concatenar tipos distintos')
except ValueError:
    print('Caracter incorrecto, ese no es un numero')
#If there is no exception goes to the else
else:
    print('Hiciste todo bien')
#What ever happens the finally block is executed
finally:
    print('Eso fue todo')

def pedir_numero():
    while True:
        try:
            number = int(input('Dame un numero: '))
        except:
            print('Ese no es un numero')
        else:
            print(f'Ingresaste el numero {number}')
            break
    print('Gracias')
pedir_numero()