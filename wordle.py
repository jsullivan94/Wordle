import random 

word_list = ['ABOUT', 'ABOVE', 'ABUSE', 'ACTOR', 'ACUTE', 'ADMIT', 'ADOPT', 'ADULT', 'AFTER', 'AGAIN', 'AGENT', 'AGREE', 'AHEAD', 'ALARM', 'ALBUM', 'ALERT', 'ALIKE', 'ALIVE', 'ALLOW', 'ALONE', 'ALONG', 'ALTER', 'AMONG', 'ANGER', 'ANGLE', 'ANGRY', 'APART', 'APPLE', 'APPLY', 'ARENA', 'ARGUE', 'ARISE', 'ARRAY', 'ASIDE', 'ASSET', 'AUDIO', 'AUDIT', 'AVOID', 'AWARD', 'AWARE', 'BADLY', 'BAKER', 'BASES', 'BASIC', 'BASIS', 'BEACH', 'BEGAN', 'BEGIN', 'BEGUN', 'BEING', 'BELOW', 'BENCH', 'BILLY', 'BIRTH', 'BLACK', 'BLAME', 'BLIND', 'BLOCK', 'BLOOD', 'BOARD', 'BOOST', 'BOOTH', 'BOUND', 'BRAIN', 'BRAND', 'BREAD', 'BREAK', 'BREED', 'BRIEF', 'BRING', 'BROAD', 'BROKE', 'BROWN', 'BUILD', 'BUILT', 'BUYER', 'CABLE', 'CALIF', 'CARRY', 'CATCH', 'CAUSE', 'CHAIN', 'CHAIR', 'CHART', 'CHASE', 'CHEAP', 'CHECK', 'CHEST', 'CHIEF', 'CHILD', 'CHINA', 'CHOSE', 'CIVIL', 'CLAIM', 'CLASS', 'CLEAN', 'CLEAR', 'CLICK', 'CLOCK', 'CLOSE', 'COACH', 'COAST', 'COULD', 'COUNT', 'COURT', 'COVER', 'CRAFT', 'CRASH', 'CREAM', 'CRIME', 'CROSS', 'CROWD', 'CROWN', 'CURVE', 'CYCLE', 'DAILY', 'DANCE', 'DATED', 'DEALT', 'DEATH', 'DEBUT', 'DELAY', 'DEPTH',]

random_word = random.choice(word_list).lower()
print("Random word:", random_word)
guesses = 6

while guesses > 0:
    user_word = input("Enter a word: ")
    if len(user_word) != len(random_word):
        print("Invalid length.")
        continue
    if user_word.upper() not in word_list:
        print("Invalid Word")
        continue
    
    updated_word = ['_'] * len(user_word)  # Initialize the updated word with underscores because it's easier

    for i in range(len(user_word)):
        if user_word[i] == random_word[i]:
            updated_word[i] = '\033[92m' + user_word[i] + '\033[0m'  # Green color for correct letter in correct position
        elif user_word[i] in random_word:
            updated_word[i] = '\033[93m' + user_word[i] + '\033[0m'  # Yellow color for correct letter in wrong position

    print(' '.join(updated_word)) #.join combines elements to a string separated by spaces

    if user_word == random_word:
        print("YOU WON!")
        break

    guesses -= 1
    print("Remaining guesses:", guesses)

    if guesses == 0:
        random_word = "\033[95m" + random_word + "\033[0m" #prints in Purple
        print("You lost. The word was", random_word)
        break

    # flex goals -- get it to not highlight yellow color if the letter has been used already
    #  get it to only use valid words i.e. words in the word_list.py DONE
    # print a word_pool of the alphabet but update it to colorize letters that you've already used
