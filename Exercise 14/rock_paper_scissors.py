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
        
game_choice = ['rock', 'paper', 'scissors']

def welcome_message(): #Welcome message
        print(f"{style.HEADER}Welcome to Rock!, Paper!, Scissors!{style.ENDC}\n")
        
        show_help()
        
def show_help(): #created the hep menu and shows the rules
        print(f"\n{style.UNDERLINE}HOW TO PLAY{style.ENDC}\nTo play the game you must type either rock, paper or scissors and press enter. The computer will randomly generate a response and the winner is the person who beats the other based on the rules. \n")
        print(f"\n{style.UNDERLINE}THE RULES {style.ENDC}\nThe rules are simple! Rock wins against scissors; paper wins against rock; and scissors wins against paper. If both players throw the same hand signal, it is considered a tie, and play resumes until there is a clear winner\n")
        print("""
Enter 'EXIT' to stop the game.
Enter 'HELP' to see how to play.
Enter 'RESTART to restart the game.
        """)
        
def start_game(): #asks the user if they are ready to start the game and if not exits

        ready_to_play = input("\nStart game? (yes / no): ")
        while ready_to_play.lower() not in ['yes', 'no']:
                ready_to_play = input("\nStart game? (yes / no): \n")
        if ready_to_play.lower() == 'yes':
                play_game()
        else:
                print("Thanks for playing!")
                
def play_game(): # creates the game and allows the user to use EXIT HELP RESTART

        player_wins = 0
        computer_wins = 0
        
        while True:
                player1_choice = input("Please type, rock, paper or scissors and press enter to begin: ")
                if player1_choice == 'EXIT':
                        print("\nThanks for playing!\n")
                        welcome_message()
                        break
                elif player1_choice == 'HELP':
                        show_help()
                        continue
                elif player1_choice == 'RESTART':
                        print('The score counter has been reset!')
                        play_game()
                elif player1_choice not in game_choice:
                        print(f"{style.WARNING} \nSorry, that was an invalid input, please try again!{style.ENDC}")
                        player1_choice = input("\nPlease type, rock, paper or scissors and press enter to begin: ")

                computer_choice = random.choice(game_choice)

                print(f"Player 1's chose {style.OKCYAN}{style.BOLD}{player1_choice}{style.ENDC}.\n ")
                print(f"The computer chose {style.OKCYAN}{style.BOLD}{computer_choice}{style.ENDC}.\n")

                # check who wins
                if player1_choice == computer_choice:
                        print(f"{style.WARNING}It's a tie!{style.ENDC}")
                elif (player1_choice == 'rock' and computer_choice == 'scissors') or (player1_choice == 'paper' and computer_choice == 'rock') or (player1_choice == 'scissors' and computer_choice == 'paper'):
                        print(f"{style.OKGREEN}Player wins!{style.ENDC}")
                        player_wins += 1
                else:
                        print(f"{style.FAIL}Computer wins!{style.ENDC} \n")
                        computer_wins += 1

                # check if someone has won best of 3
                if player_wins == 2:
                        print(f"{style.OKGREEN}Player wins best of 3!{style.ENDC}\n")
                        break
                elif computer_wins == 2:
                        print(f"{style.FAIL}Computer wins best of 3!{style.ENDC}\n")
                        break

        print(f"\nPlayer1: {player_wins} | Computer: {computer_wins}\n")

        play_again = input("\nDo you want to play again? (yes / no): \n")
        while play_again.lower() not in ['yes', 'no']:
                play_again = input("\nDo you want to play again? (yes / no): \n")
        if play_again.lower() == 'yes':
                play_game()
        else:
                print("Thanks for playing!")
                
# code to be executed when the script is run
if __name__ == '__main__':
        welcome_message()
        start_game()
        play_game()
        
#Some other nice to do features would be to add 2 players and hide the players choices, 