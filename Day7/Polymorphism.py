class Vaca:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice muuu")

class Oveja:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice beee")

vaca1 = Vaca('Aurora')
oveja1 = Oveja('Nube')

#Two objects of different classes can execute the same action.
vaca1.hablar()
oveja1.hablar()

animales = [vaca1, oveja1]

#Here the list contains different objects and they are calling different methods
#that execute different actions but with the same method name
for animal in animales:
    animal.hablar()

#Here we are using the same method with different objects, because Python can execute
# methods with the same name in different objects
def animal_habla(animal):
    animal.hablar()

animal_habla(vaca1)
animal_habla(oveja1)