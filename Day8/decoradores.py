#Las funciones son objetos
def mayuscula_saludo(texto):
    print('hola')
    print(texto.upper())
    print('Adios')


def mayuscula(texto):
    print(texto.upper())


def minuscula(texto):
    print(texto.lower())


#Ahora mi_funcion tiene como contenido mayuscula
mi_funcion = mayuscula
mi_funcion('python')


def una_funcion(funcion):
    return funcion


#Aqui llamas la funcion una_funcion que recibe como argumentto la funcion mayuscula
una_funcion(mayuscula('probando'))


#Definir funciones dentro de otras funciones
def cambiar_letras(tipo):

    def mayuscula(texto):
        print(texto.upper())

    def minuscula(texto):
        print(texto.lower())

    if tipo == 'may':
        return mayuscula
    elif tipo == 'min':
        return minuscula

operacion = cambiar_letras('may')
operacion('Palabras')

def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print('hola')
        funcion(palabra)
        print('adios')
    return otra_funcion

#Este es el decorador, que le dice a Python que cuando vaya a llamar a esta funcion la envuelva
#con este decorador
#@decorar_saludo
def mayusculas(texto):
    print(texto.upper())

@decorar_saludo
def minusculas(texto):
    print(texto.lower())

minusculas('Python')
mayusculas('Python')

#Si no queremos siempre llamar a nuestro decorador cuando se llame a mayusculas
mayusculas_decorada = decorar_saludo(mayusculas)
mayusculas_decorada('Oscar')