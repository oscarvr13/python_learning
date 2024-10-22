lista_numeros = [1, 5, 29, 83, 1, 5, 2, 19]


def reducir_lista(lista_numeros):
    set_numeros = set(lista_numeros)
    max_element = 0;
    for element in set_numeros:
        if element > max_element:
            max_element = element
    set_numeros.remove(max_element)
    return list(set_numeros)


def promedio(my_list):
    promedio = 0
    for element in my_list:
        promedio += element
    promedio = promedio / len(my_list)
    return promedio
new_list = reducir_lista(lista_numeros)
print(new_list)
promedio_value = promedio(new_list)
print(promedio_value)