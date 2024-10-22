nombre = "Carina"
# this is an error, the string is immutable can not change its content or order
#nombre[0] = "K"
print(nombre)

#Concatenate
word1 = "Kari"
word2 = "na"
print(word1 + word2)

#Multiply strings
print(word1 * 10)

# Text can be stored in the string using """
poem = """Mil pequeños peces blancos 
como si hirviera
el color del agua"""
print(poem)

# Check if exists a substring in a string
print("agua" in poem)
# Check if does not exist the substring
print("sol" not in poem)

#Check the length of the string
print(len(poem))
