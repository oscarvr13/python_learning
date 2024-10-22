class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):

    def __init__(self, nombre, apellido):
        super().__init__(nombre, apellido)
        self.cuentas = []

    def __str__(self):
        return ("El cliente {} {}\ntiene las siguientes cuentas {}"
                .format(self.nombre, self.apellido, str(self.cuentas[0])))

    def agregar_cuentas(self, cuenta):
        self.cuentas.append(cuenta)

    def obtener_cuenta(self, numero_cuenta):
        for cuenta in self.cuentas:
            if cuenta.numero_cuenta == numero_cuenta:
                return cuenta
            else:
                return ""


class Cuenta:

    def __init__(self, numero_cuenta, balance):
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def depositar(self, deposito):
        self.balance += deposito
        print('Deposito aceptado')

    def retirar(self, retiro):
        if self.balance < retiro:
            print(f"No es posible retirar {retiro}, fondos insuficientes")
        else:
            self.balance -= retiro
            print('Retiro realizado')

    def __str__(self):
        return "La cuenta {} tiene un balance {}".format(self.numero_cuenta, self.balance)

def crear_cliente():
    nombre = input("Dime el nombre del cliente: ")
    apellido = input("Dime el apellido del cliente ")
    new_cliente = Cliente(nombre, apellido)
    return new_cliente

print("Bienvenido al banco")
continuar = True
clientes = []
while continuar:
    print("Que deseas hacer\n")
    print("1) Crear cliente")
    print("2) Crear cuenta en cliente existente")
    print("3) Abonar dinero de cuenta")
    print("4) Retirar dinero de cuenta")
    print("5) Mostrar clientes")

    action = input("Indicame tu eleccion: ")

    match action:
        case "1":
            nuevo_cliente = crear_cliente()
            clientes.append(nuevo_cliente)
        case "2":
            nombre = input("Dime el nombre del cliente: ")
            apellido = input("Dime el apellido del cliente")
            cliente_escogido = ""
            for cliente in clientes:
                if cliente.nombre == nombre and cliente.apellido == apellido:
                    cliente_escogido = cliente
            if cliente_escogido != "":
                numero_cuenta = input("Dame el numero de cuenta: ")
                balance = int(input("Dame el balance: "))
                new_cuenta = Cuenta(numero_cuenta, balance)
                cliente_escogido.agregar_cuentas(new_cuenta)
            else:
                print("El cliente no existe")
        case "3":
            nombre = input("Dime el nombre del cliente: ")
            apellido = input("Dime el apellido del cliente")
            cliente_escogido = ""
            for cliente in clientes:
                if cliente.nombre == nombre and cliente.apellido == apellido:
                    cliente_escogido = cliente
            if cliente_escogido != "":
                numero_cuenta = input("Dame el numero de cuenta")
                cuenta = cliente_escogido.obtener_cuenta(numero_cuenta)
                if cuenta != "":
                    abono = int(input("Cuanto quieres abonar"))
                    cuenta.depositar(abono)
                else:
                    print("La cuenta no existe")
            else:
                print("El cliente no existe")
        case "4":
            nombre = input("Dime el nombre del cliente: ")
            apellido = input("Dime el apellido del cliente")
            cliente_escogido = ""
            for cliente in clientes:
                if cliente.nombre == nombre and cliente.apellido == apellido:
                    cliente_escogido = cliente
            if cliente_escogido != "":
                numero_cuenta = input("Dame el numero de cuenta")
                cuenta = cliente_escogido.obtener_cuenta(numero_cuenta)
                if cuenta != "":
                    retiro = int(input("Cuanto quieres retirar"))
                    cuenta.retirar(retiro)
                else:
                    print("La cuenta no existe")
            else:
                print("El cliente no existe")
        case "5":
            for cliente in clientes:
                print(cliente)
        case "6":
            action = False
