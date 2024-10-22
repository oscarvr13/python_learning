#You can store in the set only one argument
mi_set = set([1, 2, 3, 4])
print(type(mi_set))
print(mi_set)

mi_set2 = {1, 2, 3}
print(type(mi_set2))
print(mi_set2)

# You can not access the elements in the set using an index
#print(mi_set[0])
#mi_set2[0] = 5

#Only allows unique elements
mi_set2 = {1, 2, 3, 5, 1, 2}
print(mi_set2)

#this cause this error, list and dictionaries can not inserted
#TypeError: unhashable type: 'list'
#mi_set3 = {1, 2, 4, [2, 3], 5}

#tuples are allowed since these are immutable
mi_set3 = {1, 2, 3, ('hola', 'mundo') ,4 }
print(mi_set3)

#We can use the following methods
print(len(mi_set3))
#check if elements exists
print(3 in mi_set3)
#join two sets
union_set = mi_set.union(mi_set2)
print(union_set)
#Add elements to set
union_set.add(7)
print(union_set)
#Add repeated elements
union_set.add(1)
print(union_set)
#Remove one element
union_set.remove(4)
print(union_set)
#Remove non existing element
#this cause an error
#union_set.remove(10)
#Discard does not cause an error
union_set.discard(10)

#method pop deleted one of the elements,
print(union_set.pop())
print(union_set)

#Clear the set
print(union_set.clear())
print(union_set)
