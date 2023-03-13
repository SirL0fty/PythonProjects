#!/usr/bin/env python3

#imports the random module to generate a random choice for the computer
import random

#imports a style sheet to change the colours of the text by setting a style
class style:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKCYAN = '\033[96m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

#set's the options for the game
game_choice = ['rock', 'paper', 'scissors']

#Welcoe message
print(f"{style.HEADER}Welcome to Rock!, Paper!, Scissors!")

#the rules
print(f"{style.ENDC}The rules are simple! Rock wins against scissors; paper wins against rock; and scissors wins against paper. If both players throw the same hand signal, it is considered a tie, and play resumes until there is a clear winner\n")

#loop created to continue playing the game until the user quits out
while True:
        #ask the player to pick their choice
        player1_choice = input("Please type, rock, paper or scissors and press enter to begin: ")

        #validates the players choice
        while player1_choice not in game_choice:
                print(f"{style.WARNING} \nSorry, that was an invalid input, please try again!{style.ENDC}")
                player1_choice = input("\nPlease choose, rock, paper or scissors to begin: ")
        
        #randomises the computers choice
        computer_choice = random.choice(game_choice)

        #prints out the choices
        print("Player 1's chose " + style.BOLD + player1_choice + style.ENDC + ".\n ")
        print("The computer chose " + style.BOLD + computer_choice + style.ENDC + ".\n")

        #checks who wins
        if player1_choice == computer_choice:
                print(f"{style.WARNING}It's a tie!{style.ENDC}")
        elif player1_choice == 'rock' and computer_choice == 'scissors':
                print(f"{style.OKGREEN}Player 1 wins!{style.ENDC}")
        elif player1_choice == 'paper' and computer_choice == 'rock':
                print(f"{style.OKGREEN}Player 1 wins!{style.ENDC}")
        elif player1_choice == 'scissors' and computer_choice == 'paper':
                print(f"{style.OKGREEN}Player 1 wins!{style.ENDC}")
        else:
                print(f"{style.FAIL}The computer wins!{style.ENDC}")


#Some other nice to do features would be to add 2 players and hide the players choices, I could ask the player if they are ready to continue after reading the rules and also prompt a HELP section if the player forgot how to play and a done button when they wish to finishs