import random
import os
from engine import engineStart
from agreeToPlay import makeChoice
os.system('clear')
print('==========================================================================')
print("                **    **  ********  **        **            **      ")
print("               **    **  ********  **        **         **     **   ")
print("              ********  **        **        **         **      **  ")
print("             ********  ********  **        **         **      **  ")
print("            **    **  **        **        **         **      **  ")
print("           **    **  ********  ********  ********    **    **   ")
print("          **    **  ********  ********  ********       **      ")
print('==========================================================================')
print("\nWelcome to Hangman game by ILLIA\n")

name = input("\033[33m {}" .format("Enter your name: "))
print("Hello " + "\033[33m {}" .format(name) + "! Best of Luck!")
makeChoice()
