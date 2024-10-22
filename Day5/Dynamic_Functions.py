def check_number(number):
    return number in range(100, 1000)


result = check_number(1992)
print(result)


#It never returns a false so, it will return a None, the default value
#that functions return an empty object None
def check_list(my_list):
    list_3_values = []
    for n in my_list:
        if n in range(100, 1000):
            return True
        else:
            pass
    return False
result = check_list([10, 10, 3000])
print(result)
result = check_list([10, 100, 3000])
print(result)

list_3_values = []
def check_list_2(my_list):
    for n in my_list:
        if n in range(100, 1000):
            list_3_values.append(n)
        else:
            pass
    return list_3_values
result = check_list_2([10, 100, 3000])
print(result)
