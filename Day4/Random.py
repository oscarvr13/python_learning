# import all the methods from random library
from random import *

#Range of the integer
random_value = randint(1, 50)
print(random_value)

#This returns a decimal value, we can use round to specify the decimals
uniform_value = round(uniform(1, 5), 3)
print(uniform_value)

#Random choose a float number between 0 and 1
random_value = random()
print(random_value)

#Choose randomly choose an element from a list
colors = ["blue", "red", "green", "yellow"]
random_color = choice(colors)
print(random_color)

#We can use shuffel to mix the values of a list, to set the values in different order
numbers = list(range(5, 50, 5))
#Shuffle does not return a list, it modifies the object it receives as parameter
shuffle(numbers)
print(numbers)
