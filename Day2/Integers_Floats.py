my_number = 1 + 3
print(my_number + my_number)

print(type(my_number))

#Since the result is a float the final data type is a float
my_number = 5 + 5.8
print(my_number)

print(type(my_number))

# Everything you enter with the input command is considered as a string
edad = input("Dime tu edad: ")

print("Tu edad es: " + edad)

print(type(edad))

# Here you are trying to concat an int and a string
nueva_edad = 1 + edad
print("El proximo año tu edad sera: " + nueva_edad)
