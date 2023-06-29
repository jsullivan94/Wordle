from ascii import wordle_animation
import random 
from word_list import word_list
from asciialph import alph
import time

wordle_animation()

random_word = random.choice(word_list).lower()
# print("Random word:", random_word)
guesses = 6

while guesses > 0:
    user_word = input("                        Enter a word: ")
    if len(user_word) != len(random_word):
        print("                        Invalid length")
        continue

    updated_word = ['_'] * len(user_word)  # Initialize the updated word with underscores because it's easier

    for i in range(len(user_word)):
        if user_word[i] == random_word[i]:
            updated_word[i] = '\033[92m' + alph[user_word[i]] + '\033[0m'  # Green color for correct letter in correct position
        elif user_word[i] in random_word:
            updated_word[i] = '\033[93m' + alph[user_word[i]] + '\033[0m'  # Yellow color for correct letter in wrong position
        else:
            updated_word[i] = '\033[91m' + alph[user_word[i]] + '\033[0m'  # Red for not in the word

    # print(' '.join(updated_word)) #.join combines elements to a string separated by spaces
    for letter in updated_word:
        print(letter) 
        time.sleep(.25)
    

    if user_word == random_word:
        print("                         YOU WON!")
        break

    guesses -= 1
    print("                        Remaining guesses:", guesses)

    if guesses == 0:
        random_word = "\033[95m" + random_word + "\033[0m" #prints in Purple
        print("                 Out of guesses. The word was", random_word)
        break


    # flex goals -- get it to not highlight yellow color if the letter has been used already
    #  get it to only use valid words i.e. words in the word_list.py 
