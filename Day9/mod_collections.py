from collections import Counter
from collections import defaultdict
from collections import namedtuple

print('Counter ejercicios')
numeros = [8,6,9,5,4,5,5,5,8,7,4,5,4,4]

#Tenemos un diccionario con el numero de elementos que se repiten
print(Counter(numeros))

print(Counter('Mississippi'))

serie = Counter(numeros)
#Ordena en tuplas los elementos
print(serie.most_common())

#Pone los dos elementos que mas se repitan
print(serie.most_common(2))
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')

print('Default dic ejercicios')
mi_dic = {'uno':'verde', 'dos':'azul', 'tres':'rojo'}
print(mi_dic['dos'])

#Si no existe la clave que se le esta pidiendo asigna el valor nada
mi_dic_2 = defaultdict(lambda: 'nada')
mi_dic_2['uno'] = 'verde'
#Esto ya no arroja error como lo haria un diccionario normal
print(mi_dic_2['dos'])
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')

print('Tupla ejercicios')

mi_tupla = (500, 18, 65)
print(mi_tupla[1])
Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])
ariel = Persona('Ariel', 1.76, 79)
print(ariel.peso)