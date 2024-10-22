class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print('Este animal ha nacido')

    def hablar(self):
        print('Este animal emite un sonido')

class Pajaro(Animal):

#We add attributes to a sub class or child class
#We can use the super or add the attributes to the init method
    def __init__(self, edad, color, altura_vuelo):
        #self.edad = edad
        #self.color = color
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print('Pio')

    def volar(self, metros):
        print(f'El pajaro vuela {metros}')

my_animal = Animal(5, 'negro')

my_animal.hablar()

piolin = Pajaro(3, 'amarillo', 30)

#Inherited method
piolin.nacer()

#Here we overrites the inherited method hablar
piolin.hablar()

#Here we create a new method in the class Pajaro
piolin.volar(50)

