
import random
from words import words


def right_word():
    word = random.choice(words)
    while '_' in word:
        word = random.choice(words)

    return word


def to_print(x, y):
    print(f"remaining : {x}")
    print(f"Already used : {y}")


def hangman():
    word_to_guess = right_word()
    display = ''
    for i in range(len(word_to_guess)):
        display += '_'
    display = list(display)
    print(display)
    lives = 6
    t = 1
    used_letters = []
    while t:
        user_letter = input("Guess a letter : ")
        used_letters.append(user_letter)
        if user_letter in set(word_to_guess):
            print("Great!!!")
            for position in range(len(word_to_guess)):
                if list(word_to_guess)[position] == user_letter:
                    display[position] = user_letter
                    to_print(lives, used_letters)
            print(display)
            if '_' not in display:
                print("won!!!")
                t = 0

        else:
            print("Try again!!!!")
            lives -= 1
            to_print(lives, used_letters)
            if lives == 0:
                print("Sorry!!!")
                t = 0


hangman()
