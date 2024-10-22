dic = {'clave1': 100, 'clave2': 500, 'clave3': 345}

item = dic.popitem()
print(item)
item = dic.popitem()
print(item)
print(dic)

text = ',:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#'
text_m = text.lstrip(',:_#%')
print(text_m)
text_m = 'Arthur: three!'.lstrip('rthur ')
print(text_m)

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3, 'naranja')
print(frutas)

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)
print(conjuntos_aislados)