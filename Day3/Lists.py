my_list = ['a', 'b', 'c']
#The list can contain objects of different type
other_list = ['hola', 55, 66.1, True]
print(type(my_list))

result = len(other_list);
print(result)

element_at_index = other_list[0];
print(element_at_index)

#We can fetch elements from one index to another,
# Here we fetch a sublist from the index 0 to index 2 exclusive
element_at_index = other_list[0:2];
print(element_at_index)

#We can concatenate two lists
my_list2 = ['d', 'e', 'f']
my_list3 = my_list + my_list2;
print(my_list3)

#We can modify the content of a list
my_list3[0] = 'alfa'
print(my_list3)

#Different methods to modify our list
#add  element to the list
my_list3.append('g')
print(my_list3)
#delete the element of the list, if you do not specify the index deletes the last element added
deleted = my_list3.pop(0);
print(my_list3)
print(deleted)

#sort a list
list = ['f', 'z', 'a', 'm', 'c']
#sort do not return the sorted list
list.sort()
print(list)
#reverse, help us to order in reverse order
list.reverse()
print(list)


#NoneType is the result of an method that does not return anything.
# sort does not return anything.
list.sort()

