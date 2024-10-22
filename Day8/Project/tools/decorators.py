def decorar_turno(next_function):
    def agreagar_saludo():
        resultado = next_function()
        print(f"Hola su turno es {resultado}")
        print(f"Por favor espere")
    return agreagar_saludo



