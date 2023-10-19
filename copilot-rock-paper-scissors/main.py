# Write a rock, paper, scissors game

# Import random module
import random

# define main function that handles all the logic
def main(): 
    # Display the game's title
    print("Let's play Rock, Paper, Scissors!")
    
    # Create a variable to control the loop
    again = 'y'
    
    # Create a loop to control the game
    while again == 'y' or again == 'Y':
        # Get the user's choice
        user_choice = get_user_choice()
        
        # Get the computer's choice
        computer_choice = get_computer_choice()
        
        # Determine the winner
        winner = determine_winner(user_choice, computer_choice)
        
        # Display the winner
        display_winner(winner)
        
        # Do this again?
        again = input('Do you want to play again? (y = yes): ')

def display_winner(winner):
    # Display the winner
    if winner == 'user':
        print('You win!')
    elif winner == 'computer':
        print('The computer wins!')
    else:
        print('The game was a tie.')

def determine_winner(user_choice, computer_choice):
    # Determine the winner
    if user_choice == computer_choice:
        winner = 'tie'
    elif user_choice == 'rock':
        if computer_choice == 'paper':
            winner = 'computer'
        else:
            winner = 'user'
    elif user_choice == 'paper':
        if computer_choice == 'scissors':
            winner = 'computer'
        else:
            winner = 'user'
    else:
        if computer_choice == 'rock':
            winner = 'computer'
        else:
            winner = 'user'
    # Return the winner
    return winner

def get_user_choice():
    # Get the user's choice
    user_choice = input('Enter rock, paper, or scissors: ')
    # Validate the choice
    while user_choice != 'rock' and user_choice != 'paper' and user_choice != 'scissors':
        print('Error: Invalid choice')
        user_choice = input('Enter rock, paper, or scissors: ')
    # Return the user's choice
    return user_choice

def get_computer_choice():
    # Get the computer's choice
    computer_choice = random.randint(1, 3)
    # Determine the computer's choice
    if computer_choice == 1:
        computer_choice = 'rock'
    elif computer_choice == 2:
        computer_choice = 'paper'
    else:
        computer_choice = 'scissors'
    # Return the computer's choice
    return computer_choice


#Call main function
main()