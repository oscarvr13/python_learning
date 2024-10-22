from random import *

name = input("What is your name: ")
tries = 8
choosen_number = randint(1, 256)
#print(choosen_number)
print(f"Hello {name} I have got a number between 1 and 100 and you need to guess it, "
      f"you only have {tries} tries")
while tries > 0:
    number = int(input("Tell me the number: "))
    if number < 1 or number > 256:
        print(f"The number {number} is not allowed please try another number")
        print("This is not considered a failed try")
        continue
    elif number < choosen_number:
        tries -= 1
        print(f"Your answer is incorrect the number {number} is lesser than my number,"
              f" you now have {tries} attempts")
    elif number > choosen_number:
        tries -= 1
        print(f"Your answer is incorrect the number {number} is greater than my number,"
              f" you now have {tries} attempts")
    else:
        tries -= 1
        print(f"You win, it takes you {8 - tries} attempts")
        break

print(f"The secret number is {choosen_number}")