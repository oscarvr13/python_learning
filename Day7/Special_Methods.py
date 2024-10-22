my_list = [1, 1, 1, 1, 1]
print(len(my_list))


class ObjectClass:
    pass


# <__main__.ObjectClass object at 0x7f2072e4a290>
#String representation of this ObjectClass instance
my_object = ObjectClass()

print(my_object)


class CD:

    def __init__(self, author, titulo, canciones):
        self.author = author
        self.titulo = titulo
        self.canciones = canciones

    #Here we change the str method
    def __str__(self):
        return f'Album: {self.titulo} de {self.author}'

    #We can define the special method len
    def __len__(self):
        return self.canciones

    def __del__(self):
        print(f"Se ha eliminado el cd {self.titulo}")

my_cd = CD('Pink Floyd', 'The wall', 24)

print(f'canciones :{len(my_cd)}')
#This is the same as doing this str(my_cd)
print(my_cd)

#The my_cd object does not exist anymore
del my_cd
#This throws an error since the object is already deleted
# print(my_cd)