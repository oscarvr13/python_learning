my_tuple = (1, 2, 3, 4)
print(type(my_tuple))

my_tuple2 = (1, 1.5, "Hola", False)
print(my_tuple2)

#Check the index 0
print(my_tuple2[2])

#Tuples are immutable this is not allowed
#my_tuple2[0] = 5

my_tuple3 = (1, 2, (10, 20), 3 ,4)
#Check the inner tuple at the index 2, and check the index 0 of this inner taple
print(my_tuple3[2][0])

#Convert a tuple to list
my_tuple3 = list(my_tuple3)
print(type(my_tuple3))

#Convert a list to tuple
my_tuple3 = tuple(my_tuple3)
print(type(my_tuple3))

my_tuple4 = (1, 2, 3)
#We can unpack the tuples, list or dictionaries assigning directly to the variables
x, y, z = my_tuple4
print(x, y, z)

my_tuple5 = (1, 2, 3, 1)
#Count the occurences of the element
print(my_tuple5.count(1))
#Check the indexOf the values provided
print(my_tuple5.index(2))