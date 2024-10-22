class Animal:

    def __init__(self, edad, color):
        self.color = color
        self.edad = edad
    def nacer(self):
        print("Este animal ha nacido")

#Inherits from Animal class
class Pajaro(Animal):
    pass



#This property tell us which class inherits from
print(Pajaro.__bases__)
#This property tell us the class which are subclasses of Animal
print(Animal.__subclasses__())

#The constructor is inherited and hides the default constructor
piolin = Pajaro(2, 'amarillo')
#this method is inherited from Animal
piolin.nacer()
#Pajaro inherits the instance properties from Animal, edad and color
print(f"Piolin tiene {piolin.edad} años y color {piolin.color}")