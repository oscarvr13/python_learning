num1 = 20
num2 = 30.5

print(type(num1))


# Here num1 becomes a float, implicit conversion
num1 = num1 + num2

print(type(num1))
print(type(num2))

num1 = 5.8
print(num1)
print(type(num1))

# truncate the decimal part, it does not round up or down the value
num2 = int(num1)
print(num2)
print(type(num2))

edad = input("Dime tu edad: ")
print(type(edad))
edad = int(edad)
nueva_edad = 1 + edad
# Here you can not concatenate an int to string
print("Nueva edad: " + str(nueva_edad))