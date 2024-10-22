min_value = min(58, 96, 72, 64, 35)
print(min_value)

max_value = max(58, 96, 72, 64, 35)
print(max_value)

my_list = [12, 350, 1, 98, 54]
max_value = max(my_list)
min_value = min(my_list)
print(f"Max value is {max_value} and min value is {min_value}")

names = ["Juan", "Pablo", "Alicia", "Carlos"]
print(min(names))
print(max(names))

#Remember there is a difference between lower and upper characters
#so for python A > z so you should use lower
name = "fernAnd"
print(min(name))
print(max(name))

#For dictionaries it looks by default the lowest key
dic = {"C1": 45, "C2" : 11}
print(min(dic))
print(min(dic.values()))




