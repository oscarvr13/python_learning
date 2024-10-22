class Pajaro_2:

    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Puso {cantidad} huevos")
        #This method can not access the instance attributes
        #We do not receive self, receive cls
        #print(f"Es de color {self.color}")
        cls.alas = False
        print(f"Tiene alas ? {Pajaro_2.alas}")

#This method can be called directly by the class
Pajaro_2.poner_huevos(4)
