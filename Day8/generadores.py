def my_function():
    lista = []
    for x in range(1, 5):
        lista.append(x * 10)
    return lista


def mi_generador():
    for x in range(1, 5):
        yield x * 10


print(my_function())
print(mi_generador())

g = mi_generador()

print(next(g))
print(next(g))
print(next(g))
print(next(g))


#This causes an error since the next number can not be generated
#print(next(g))

def generador_2():
    #each next call, receives a yield value
    x = 1
    yield x

    #each next call, receives a yield value
    x += 1
    yield x

    #each next call, receives a yield value
    x += 1
    yield x


g_2 = generador_2()
print(next(g_2))
print(next(g_2))
print('Last number')
#This remembers the last number generated
print(next(g_2))


def generador_infinito():
    init_value = 0
    while (True):
        init_value += 1
        yield init_value


generador = generador_infinito()

print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))


def generador_infinito_multiplos7():
    init_value = 0
    while (True):
        init_value += 7
        yield init_value

generador = generador_infinito_multiplos7()

print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))


def generador_perder_vida():
    vidas = 3
    while(vidas > 1):
        yield f"Te quedan {vidas} vidas"
        vidas -= 1
    if vidas == 1:
        yield f"Te queda {vidas} vida"
        vidas -= 1
    yield 'Game Over'

perder_vida = generador_perder_vida()
#El generador ejecuta el codigo por partes y recuerda en que parte del codigo se quedo
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
#print(next(perder_vida))
