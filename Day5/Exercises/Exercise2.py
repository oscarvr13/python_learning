'''
Escribe una función (puedes ponerle cualquier nombre que
quieras) que reciba cualquier palabra como parámetro, y que
devuelva todas sus letras únicas (sin repetir) pero en orden
alfabético.
Por ejemplo si al invocar esta función pasamos la palabra
"entretenido", debería devolver ['d','e','i','n','o','r','t']
'''

def check_word(palabra):
    #We need to lower all the characters since A is not equal to a
    palabra = palabra.lower()
    chars = set()
    for char in palabra:
        chars.add(char)
    list_chars = list(chars)
    list_chars.sort()
    return list_chars

sorted_chars = check_word('cascarrabias')
print(sorted_chars)
