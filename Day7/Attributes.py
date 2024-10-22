class Pajaro:

    #alas is a class attribute for all the classes
    alas = True

    # Pajaro constructor
    # each time you create an object you call the constructor
    # self is the instance of the class you are about to create

    #color is the parameter
    def __init__(self, color_param, especie):
        # self is the instance we are about to create
        # self.color is the attribute of the class, color is the attribute
        self.color_attr = color_param
        self.especie = especie

#Now we need to pass the parameter
my_pajaro = Pajaro("azul", 'Tucan')
print(Pajaro.alas)
print(my_pajaro.alas)

palabra = 'hola'

print(f"Mi pajaro es un {my_pajaro.especie}  de color {my_pajaro.color_attr}")