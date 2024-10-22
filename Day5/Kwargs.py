def suma(**kwargs):
    print(type(kwargs))
#This is not a dictionary but it becomes a dictionary when call the suma function
suma(x=3, y=5, z=2)

def suma_2(**kwargs):
    total = 0
    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor
    return total

total = suma_2(x=3, y=5, z=2)
print(total)

def suma_3(num1, num2, *args, **kwargs):
    print(f'El primer valor es {num1}')
    print(f'El segundo valor es {num2}')

    for arg in args:
        print(f"arg = {arg}")

    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")
    lista = list(kwargs.values())
    print(lista)

suma_3(15, 20, 45, 67, 83, 82, x='uno', y='dos', z='tres')

args = [45, 67, 83, 82]
kwargs = {'x':'uno', 'y':'dos', 'z':'tres'}
#We pass the list and the dictionary and adding the * and ** we transform into args and kwargs
suma_3(15, 50, *args, **kwargs)

