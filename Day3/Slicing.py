texto = "ABCDEFGHIJKLM"
# from index 2 to index 5 exclusive
substring = texto[2 : 5]
print(substring)

# from index 2 to end
substring = texto[2:]
print(substring)

# from beginning of the string till index 5 exclusive
substring = texto[:5]
print(substring)

# from index 2 to index 10 exclusive, extract each two characters
substring = texto[2 : 10 : 2]
print(substring)

# from index 0 to  last index , extract each 3 characters
substring = texto[::2]
print(substring)

# reverse the string
substring = texto[::-1]
print(substring)