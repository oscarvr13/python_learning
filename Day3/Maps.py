map1 = {'c1' : 'value1', 'c2' : 'value2'}
#data type dict
print(type(map1))
print(map1)

#using the key we can retrieve the values
result = map1['c1']
print(result)

map_client = {'name' : 'Juan', 'lastName' : 'Fuentes', 'weight' : 80, 'height' : 1.76}
client = map_client['lastName']
print(client)

#The dictionaries can include lists of other dictionary
new_map = {'c1' : 55, 'c2' : [10, 20, 30], 'c3': {'s1' : 100, 's2':200}}
print(new_map['c2'])
#check the list in the c2 the index 1
print(new_map['c2'][1])

#Check the value in the c3 key and in the fetched dic take the element at the key s2
print(new_map['c3']['s2'])

dic = {'c1':['a', 'b', 'c'], 'c2':['d', 'e','f']}
print(dic['c2'][1].upper())
#Add new key - value to an existing dic
dic['c3'] = ['g', 'h', 'i']
print(dic)
# Modify the dic
dic['c1'] = ['A', 'B', 'C']
print(dic)
#Check all the keys inside the dict
print(dic.keys())
#Check all the values
print(dic.values())
#Check keys and values
print(dic.items())



