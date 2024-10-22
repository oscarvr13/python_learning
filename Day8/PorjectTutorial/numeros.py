def numeros_perfurmeria():
    for n in range (1, 10000):
        yield f'P - {n}'

def numeros_farmacia():
    for n in range (1, 10000):
        yield f'F - {n}'

def numeros_cosmetica():
    for n in range (1, 10000):
        yield f'C - {n}'

function_perfumeria = numeros_perfurmeria()
function_farmacia = numeros_farmacia()
function_cosmetica = numeros_cosmetica()

def decorador(rubro):
    print('\n' + '*' * 23)
    print('Su numero es:')
    if rubro == 'P':
        print(next(function_perfumeria))
    elif rubro == 'F':
        print(next(function_farmacia))
    else:
        print(next(function_cosmetica))
    print('Aguarde y sera atendido')
    print('*' * 23 + '\n')

