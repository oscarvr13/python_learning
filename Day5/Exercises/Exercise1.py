#Exercise 1
'''Crea una función llamada devolver_distintos() que reciba 3
integers como parámetros.
Si la suma de los 3 numeros es mayor a 15, va a devolver el
número mayor.
Si la suma de los 3 numeros es menor a 10, va a devolver el
número menor.
Si la suma de los 3 números es un valor entre 10 y 15
(incluidos) va a devolver el número de valorintermedio.'''

def devolver_distintos(*args):
    total = 0
    for arg in args:
        total += arg
    if total > 15:
        return max(args)
    elif total < 10:
        return min(args)
    else:
        my_list = list(args)
        my_list.sort()
        return my_list[1]

# result < 15 and >= 10
result = devolver_distintos(6, 1, 5)
print(result)

#result > 15
result = devolver_distintos(6, 10, 5)
print(result)

#result < 10
result = devolver_distintos(3, 1, 5)
print(result)
