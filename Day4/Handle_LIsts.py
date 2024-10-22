word = "python"
list_var = []

for char in word:
    list_var.append(char)
print(list_var)

#Better way to do it
list_var = [char for char in word]
print(list_var)
list_var = [char for char in "java"]
print(list_var)

#Create list containing numbers
list_var = [n / 2 for n in range(0,21,2)]
print(list_var)

#We can incorporate an if sentence
#Add only the numbers that meet the condition
list_var = [n if n * 2 > 10 else 'no' for n in range(0,21,2)]
print(list_var)

foot = [10, 20, 30, 40, 50]
meters = [number_feet * 0.3048 for number_feet in foot]
print(meters)