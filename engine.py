import random
import time
import string
from stagedecoration import printState

# Here we need to open a file, make random  choice and return word: 
def word_selected(file):
    word_file = open(file,'r+')
    secret_word = random.choice(word_file.read().split())
    word_file.close()
    return secret_word
# This function makes' stars, check's players words and insert it inside the gueseed word:
def engineStart():
    secretword = word_selected('hangman.txt')
    alfabet = list(string.ascii_lowercase)
    def word_selected_dashed():
        word_selected_dashed = []
        for i in range(len(secretword)):
            if secretword[i] in alfabet:
                word_selected_dashed.append('*')
            else: word_selected_dashed.append(secretword[i])
        return ''.join(word_selected_dashed)
    word_selected_dashed = word_selected_dashed()
    print(word_selected_dashed)
# Here we start counting trials:
    trials = 6
    all_User_guseed_letters = []
    gussed_word = list(word_selected_dashed)
# The first part of the main block. We check player's letters. Is it equal or not.
    while trials > 0:
        if ''.join(gussed_word) == secretword:
            print("\033[32m {}".format("Congraluation, you have gussed the correct word"))
            break
        print('You have got '+ str(trials)+ ' wrong tries. Put a letter ')
        user_guseed_letter = input("Put your letter here: ")
# If the player put the same letter we will notify him:
        if user_guseed_letter in all_User_guseed_letters:
            print("You've already put this letter, put another one! ")
        else:
            if user_guseed_letter in secretword and len(user_guseed_letter) > 0:
                print("\033[32m {}".format('Great!'))
                all_User_guseed_letters.append(user_guseed_letter)
                if user_guseed_letter in all_User_guseed_letters:
                    print("You've already put correct letter, put another one! ")
# In this block we insert player's letter into secret word by index:
                for i in range(len(secretword)):
                    if list(secretword)[i] == user_guseed_letter:
                        gussed_word[i] = user_guseed_letter
                        print(''.join(gussed_word))
# The second part of the main block. If player's letters is not correct we will notify the player:
            elif user_guseed_letter not in secretword:
                print("\033[31m {}".format('Wrong! Try again. You should put only 1 letter'))
                trials -= 1
                printState(trials)
# If trials equal zero - The Game is over :)
    if trials == 0 :
        print("\033[31m {}".format('You have ran out of trials, the secret word was ' + "\033[34m {}".format(secretword)))   

