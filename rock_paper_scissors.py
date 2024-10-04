#--------------------------------------------------------------------------------------------------------#
#---------------------------------- ROCK-PAPER-SCISSORS-GAME --------------------------------------------#

import random

def computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def user_choice():
    while True:

        user_input = input("Enter rock, paper, or scissors: ").lower()

        if user_input in ['rock', 'paper', 'scissors']:
            return user_input
        print("Invalid choice. Please enter rock, paper, or scissors.")

def determine_winner(U_choice, C_choice):

    if U_choice == C_choice:
        return "It's a tie!"
    
    elif (U_choice == 'rock' and C_choice == 'scissors') or \
         (U_choice == 'paper' and C_choice == 'rock') or \
         (U_choice == 'scissors' and C_choice == 'paper'):
        return "You win!"
    
    else:
        return "You lose!"

def play_game():

    print("Welcome to Rock, Paper, Scissors!")
    U_choice = user_choice()
    C_choice = computer_choice()
    
    print("\nYour choice: ",U_choice)
    print("Computer's choice: ",C_choice)
    
    result = determine_winner(U_choice, C_choice)
    print(result)


if __name__ == "__main__":
    play_game()
