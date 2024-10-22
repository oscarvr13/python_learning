text = "Este es el texto Federico"
result = text[2:10].upper()
print(result)

# lower case
result = text[2:10].lower()
print(result)

# split using as separator the blank space " "
result = text.split()
print(result)

# split using as separator the blank space "t"
result = text.split("t")
print(result)

# join the elements
text1 = "Aprender"
text2 = "Python"
text3 = "es"
text4 = "genial"
join_character = "_"
# create the list to pass as argument to join
result = join_character.join([text1, text2, text3, text4])
print(result)

# find method if the character does not exist returns -1
result = text.find("tex")
print(result)

#replace Federico for todos
result = text.replace("Federico", "todos").replace("e", "x")
print(result)
result = text.replace("e", "x")
print(result)



