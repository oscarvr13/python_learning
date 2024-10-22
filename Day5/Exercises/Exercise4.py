'''
Escribe una función llamada contar_primos() que requiera un
solo argumento numérico.
Esta función va a mostrar en pantalla todos los números
primos existentes en el rango que va desde cero hasta ese
número incluido, y va a devolver la cantidad de números
primos que encontró.
Aclaración, por convención el 0 y el 1 no se consideran primos
'''

def contar_primos(number):
    my_divisor = {2, 3, 5, 7}
    cantidad_primos = 0
    #Remember the limits range is (inclusive, exclusive)
    for number in range(0, number):
        if number == 0 or number == 1:
            continue
        is_primo = True;
        for divisor in my_divisor:
            if number % divisor == 0:
                #Unless it is the same number as divisor
                #Example 2 3 5 7
                if number not in my_divisor:
                    is_primo = False
                    break
        if is_primo:
            print(number)
            my_divisor.add(number)
            cantidad_primos += 1
    return  cantidad_primos

cantidad = contar_primos(151)
print(f'Cantidad primos {cantidad}')