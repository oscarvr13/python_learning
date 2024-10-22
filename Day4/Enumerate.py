my_list = ['a', 'b', 'c']
index = 0

for item in my_list:
    print(item, index)
    index += 1

#Now the item object contains the index and the object
for index, item in enumerate(my_list):
    print(f"At index {index} is the element {item}")

#Now the item object contains the index and the object
for index, item in enumerate(range(0, 11, 2)):
    print(f"At index {index} is the element {item}")

my_tuples = list(enumerate(my_list))
print(my_tuples)
#We can print elements individually
print(my_tuples[1][0])


