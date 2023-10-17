from ascii_wordle import wordle_animation
import random 
from word_list import word_list
from ascii_alph import alph
import time
import user

wordle_animation()
def sign_up_in():
    sign_up_or_in = input("        Signup or Login or play?: signup/login/play ")
    if sign_up_or_in == "login":
        user.Sign_In()
        main()
    elif sign_up_or_in == "signup":
        user.Sign_up()
        main()
    else:
        main()
       
def main():
    random_word = random.choice(word_list).lower()
    # print("                        Random word:", random_word)
    guesses = 6
    used_letters = set()
    while guesses > 0:
        user_word = input("                        Enter a word: ")
        if len(user_word) != len(random_word):
            print("                        Invalid length")
            continue

        updated_word = ['_'] * len(user_word) 
        
        for i in range(len(user_word)):
            if user_word[i] == random_word[i]:
                updated_word[i] = '\033[92m' + alph[user_word[i]] + '\033[0m'  
            elif user_word[i] in random_word:
                updated_word[i] = '\033[93m' + alph[user_word[i]] + '\033[0m'  
            else:
                updated_word[i] = '\033[91m' + alph[user_word[i]] + '\033[0m' 
                used_letters.add(user_word[i])
        for letter in updated_word:
            print(letter) 
            time.sleep(.25)

        if user_word == random_word:
            print('\033[0;32m'r"""

             _  _  _____  __  __    _    _  _____  _  _ /\
            ( \/ )(  _  )(  )(  )  ( \/\/ )(  _  )( \( ))(
             \  /  )(_)(  )(__)(    )    (  )(_)(  )  ( \/
             (__) (_____)(______)  (__/\__)(_____)(_)\_)()
                    
            
                                                                                           
          
                             """'\033[0m') 
            if user.signedIn == True:
                user.Update_streak()
                user.call_streak()
            else:
                pass
            main() 
            break

        guesses -= 1
        print("                        Remaining guesses:", guesses)
        print("                        Wrong letters:", used_letters    )

        if guesses == 0:
            user.decrement_streak()
            random_word = "\033[95m" + random_word + "\033[0m" 
            print("                 Out of guesses. The word was", random_word)
            main() 
            break

if user.globalUsername == None:     
    sign_up_in()
else:
    main()
