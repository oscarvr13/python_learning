precios_cafe = [('capuchino', 1.5), ('Expresso', 2.2),
                ('Moka', 1.9)]
for cafe, precio in precios_cafe:
    print(precio * 0.45)

def cafe_mas_caro(lista_precios):
    precio_max = 0
    cafe_max = ''

    for cafe, precio in lista_precios:
        if precio > precio_max:
            precio_max = precio
            cafe_max = cafe
    return (cafe_max, precio_max)

cafe, precio = cafe_mas_caro(precios_cafe)
print(f"El cafe mas caro es {cafe} cuyo precio es {precio}")
