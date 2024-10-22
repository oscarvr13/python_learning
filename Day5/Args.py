def suma(a,b):
    return a + b
result = suma(5,6,)
print(result)

def suma_generic(*args):
    total = 0
    for arg in args:
        total += arg
    return total
result = suma_generic(5,6,7)
print(result)


