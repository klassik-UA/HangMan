from engine import engineStart
import os
def makeChoice():
    choice = input("\033[37m {}".format("The game is about to start!\n Let's play Hangman! Press \"yes\" to start or \"no\" to quit: "))
    while choice == "yes":
        engineStart()
        choice = input("\033[37m {}".format("Do you want to play again? yes/no "))
        os.system('clear')
        if choice == 'no':
            break
    while choice == "no":
        print("Ok, Good Luck!")
        break       
    else: 
        print(' You should choose between "yes" or "no"')
        makeChoice()
