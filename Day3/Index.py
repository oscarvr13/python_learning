mi_texto = "Esta es una prueba"
resultado = mi_texto[9]
#Should store the character E
print(resultado)

# We can use a negative number an then python will count from right to left
# the first character at the left will be always the zero index
resultado = mi_texto[-4]
#Should store the character u
print(resultado)

# Look for a charcater in our string, the character n is at index 9
# if the character does not exist throws an error
# returns always the first occurrence
mi_texto = "Esta es una prueba"
resultado = mi_texto.index("a")
print(resultado)

#We can look for the character but not in the whole string we can choose a portion of the string
resultado = mi_texto.index("a", 5, 15)
# print 10 since the first occurrence of a is not between the (5, 15) range
print(resultado)

# returns the start index of the word you are looking for
# index method is case sensitive
resultado = mi_texto.index("prueba")
print(resultado)

# the method rindex lookf fot the character from left to right
resultado = mi_texto.rindex("a")
# return the last occurrence.
print(resultado)