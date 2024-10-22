#Program a text analyzer
#First the user needs to enter a text
#After the program needs to receive three characters
# Using these three characters and the text, the program should return the following info
#1.- How many times each character is in the text (no case sensitive)
#2.- How many words are in the whole text
#3.- Inform the first character and the last one
#4.- Show the text in reverse order only the words not the character inside the words
#5.- Check if the word python appears in the text

text = input("Introduce the text to analyze please: ").lower()
characters = input("Introduce the three characters to check in the text separated by blank space: ")
char1 , char2, char3 = characters.lower().split(" ")
char1_counter = text.count(char1)
char2_counter = text.count(char2)
char3_counter = text.count(char3)

print(f"Character {char1} appears {char1_counter} times")
print(f"Character {char2} appears {char2_counter} times")
print(f"Character {char3} appears {char3_counter} times")

text_list = text.lower().split(" ")
count_total_words = len(text_list)
print(f"Total worlds are {count_total_words}")

# We use the string and fetch the first and last character
first_char = text[0]
last_char = text[-1]
print(f"First character is {first_char} and last character is {last_char}")

# Reverse the whole list and join the elements using the join method
text_list.reverse()
reverse_text = " ".join(text_list)
print(f"Reverse text :\n {reverse_text}")

is_python_word = "python" in text
print(f"Is the word python in the list {is_python_word}")
