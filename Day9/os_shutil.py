import os
import shutil
#Gives you the directory you are working on
print(os.getcwd())

archivo = open('curso.txt', 'w')
archivo.write('texto de prueba')
archivo.close()

#Move a file from one directory to another
#shutil.move('curso.txt', "/home/oscar/Documents")

ruta = "/home/oscar/Documents"

for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f'En la carpeta: {carpeta}')
    print(f'Las subcarpetas son:')
    for sub in subcarpeta:
        print(f'\t{sub}')
    print('Los archivos son:')
    for arch in archivo:
        print(f'\t{arch}')
    print('\n')