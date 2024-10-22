class Pajaro:

    alas = True

#Instance methods
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        #We need to use the color of the instance that is calling this method, for that we use self
        print("Pio, mi color es {}". format(self.color))

    def volar(self, metros):
        print(f"El pajaro ha volado {metros}, metros")
        #We can access other methods
        self.piar()
        #We can modify the state of the class
        Pajaro.alas = False

    #Instance methods modify the attributes of the object
    def pintar_negro(self):
        self.color = 'negro'

piolin = Pajaro("amarillo", "canario")
piolin.piar()
piolin.volar(4)
print(f"Piolin tiene alas : {Pajaro.alas}")
piolin.pintar_negro()
piolin.volar(50)


print(piolin.alas)
