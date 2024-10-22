'''
Escribe una función que requiera una cantidad indefinida de
argumentos. Lo que hará esta función es devolver True si en
algún momento se ha ingresado al numero cero repetido dos
veces consecutivas.
Por ejemplo:
(5,6,1,0,0,9,3,5) >>> True
(6,0,5,1,0,3,0,1) >>> False
'''


def consecutive_repeat_number(*args):
    prev_number = -1;
    for arg in args:
        if prev_number == 0 and arg == 0:
            return True
        else:
            prev_number = arg
    return False


print(consecutive_repeat_number(5, 6, 1, 0, 0, 9, 3, 5))
print(consecutive_repeat_number(6, 0, 5, 1, 0, 3, 0, 1))
