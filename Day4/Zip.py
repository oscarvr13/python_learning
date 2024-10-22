names = ['Ana', 'Hugo', 'Valeria']
ages = [65, 49, 42]

combine_list = list(zip(names, ages))

#This prints the object and the memory address you need to cast it to list
print(combine_list)

# Remember only takes the shortest list and combine the elements
#in this case only takes the names list and combine with the ages, and leave out the elements
#that do not have a pair.
ages = [65, 49, 42, 55]
combine_list = list(zip(names, ages))
#This prints the object and the memory address you need to cast it to list
print(combine_list)

#Now we have the combination of the three lists
cities = ["Lima", "Madrid", "Mexico"]
combine_list = list(zip(names, ages, cities))
print(combine_list)

for name, age, city in combine_list:
    print(f"name {name} is  {age} years old and lives in {city}")

