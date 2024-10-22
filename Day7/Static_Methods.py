class Pajaro_3:
    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    @staticmethod
    #These methods do not refer to the class or the instance, we can not modify
    #the state of the class or the instance
    def mirar():
        #This is an error, we can not call instance attributes or class attributes
        #self.color = 'Guinda'
        #cls.alas = False
        print("We can not call to change class or instance attributes")
        #We do not want to modify any isntance attribute or class
        print("El pajaro mira")


#We can calling without using an object
Pajaro_3.mirar()
