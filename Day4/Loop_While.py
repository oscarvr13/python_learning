coins = 5
while (coins > 0):
    print(f"I have {coins} coins")
    coins -= 1
else:
    print("I do not have coins")

init_value = "s"
while init_value == "s":
    init_value = input("Do you want to continue? (s/n): ")
else:
    print("Ok, thanks and have a good day")

#Key word pass
while init_value == "s":
    #Just avoid the while and pass to the next line of code
    pass
print("hola")

#key word break, to interrup the loop
name = input("Enter your name: ")
for char in name:
    if (char == 'r'):
        break
    print(char)
print()
for char in name:
    if char == 's':
        #This returns directly to the iteration again omitting process this value
        continue
    print(char)