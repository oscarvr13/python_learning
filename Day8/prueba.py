import unittest
import cambia_texto

#Necesitamos heredar de unittest TestCase class
class ProbarCambiaTexto(unittest.TestCase):

    #The functions needs to start with the test word
    def test_mayusculas(self):
        palabra = 'buen dia'
        resultado = cambia_texto.todo_mayusculas(palabra)
        self.assertEquals(resultado, 'BUEN DIA')

'''
Antes incluso de ejecutar el código, Python lee el archivo para definir algunas variables globales. 
Una de ellas es__name__, que toma el nombre "__main__" en caso que Python esté corriendo en dicho
 módulo de manera individual. Si por el contrario, el módulo fuera importado, la variable __name__ 
 toma el nombre del módulo. Este bloque de código evalúa que la prueba se esté ejecutando directamente.
'''
if __name__ == '__main__':
    unittest.main()