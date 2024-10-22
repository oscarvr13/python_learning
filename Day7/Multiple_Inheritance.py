class Father:
    def talk(self):
        print(f'Hola')


class Mother:

    def laugh(self):
        print('ja ja ja')

    def talk(self):
        print(f'que tal')

#Multiple inheritance
class Son(Father, Mother):
    pass


class GrandSon(Son):
    pass


my_grandSon = GrandSon()

#GrandSon can talk because inherits the method from Father through Son (not directly)
#The method that inherits first (talk from Father )takes precedence over the method inherits from Mother
my_grandSon.talk()
#GrandSon inherits the method laugh from Mother and thorugh son
my_grandSon.laugh()

#Method order resolution, the order in which is resolved the methods
print(GrandSon.mro())
#output
#[<class '__main__.GrandSon'>, <class '__main__.Son'>, <class '__main__.Father'>, <class '__main__.Mother'>, <class 'object'>]
#Firts checks the GrandSon, Son, Father, Mother and lastly Object class