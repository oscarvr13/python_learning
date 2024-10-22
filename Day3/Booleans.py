mi_bool_1 = True
mi_bool_2 = False
print(type(mi_bool_1))
print(mi_bool_1)

#
number = 5
# Create an expression that returns a boolean
result = number > (2 + 3)
print(result)

result = number >= (2 + 3)
print(result)

#Create the boolean
result = bool(5 > 6)
print(result)

#this is false
result = bool()
print(result)

list_1 = [1, 2, 4, 5]
exists_5 = 5 in list_1
print(exists_5)
