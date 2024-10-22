from random import *



def get_word():
    words = ['perro', 'arbol', 'murcielago', 'ave']
    return choice(words)


def create_ahorcado(word):
    ahorcado = ['-'] * len(word)
    return ahorcado

def ask_for_character():
    is_not_valid = True
    while(is_not_valid):
        char = input("Please tell me the character: ")
        if char.isalpha() and len(char) == 1:
            return char.lower()
        else:
            print(f"The characater {char} is not valid please enter a correct caracter")

def check_character_in_word(char, word, ahorcado):
    char_is_in_word = False
    for i in range(len(word)):
        if word[i] == char:
            ahorcado[i] = char
            char_is_in_word = True
    return char_is_in_word

lifes = 5

print("Hello this is a game called ahorcado\n"
      "In this game you need to guess each character of the word \n"
      "You can only see each characater as a -")
word = get_word()
ahorcado = create_ahorcado(word)
while (lifes > 0):
    print(f"You have {lifes} lives")
    print(f"This is your world {ahorcado}")
    char = ask_for_character()
    is_char_in_word = check_character_in_word(char, word, ahorcado)
    if not is_char_in_word:
        lifes -= 1
        print(f"You lost one life now you have {lifes} lifes")
    if '-' not in ahorcado:
        print("Congratulations you win the game")
        print(f"The word is {ahorcado}")
        break
if lifes == 0:
    print(f"You lost the game, the word is {word}")