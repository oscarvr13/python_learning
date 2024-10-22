list_numbers = [1, 2, 3, 4]
for number in list_numbers:
    print(number)

#Range starts in 0 by default the syntax is (inclusive, exclusive)
for number in range(1, 31):
    print(number)

#Here counts from 0 to 30, counting 3 by 3
for number in range(0, 31, 3):
    print(number)

#We can use range to create a list
list_numbers = list(range(0 , 101, 10))
print(list_numbers)

