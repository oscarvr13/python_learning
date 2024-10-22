lista = ['a', 'b', 'c', 'd']

for element in lista:
    index = lista.index(element) + 1
    print(f"character at index {index} is {element}")

lista = ["Pablo", "Maria", "Fede", "Laura"]
for name in lista:
    if (name.lower().startswith("l")):
        print(f"The name {name} starts with l")
    else:
        print(f"The name {name} does not start with l")

numbers = [1, 2, 3, 4, 5]
my_value = 0
for number in numbers:
    my_value = my_value + number
print(f"last_value is {my_value}")

palabra = "Python"

for char in palabra:
    print(f"print each character: {char}")

for char in "Java":
    print(f"print each character: {char}")

for number_list in [[1,2], [3,4], [5, 6]]:
    for number in number_list:
        print(number)
dic = {"key1":'a', "key2":'b', "key3":'c'}

#this prints the key value pair
for key, value  in dic.items():
    print(f"The key is {key} and the value is {value}")

#this prints only the keys
for key  in dic:
    print(f"The key is {key}")
#this prints the values
for value in dic.values():
    print(value)
