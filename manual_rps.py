import random

def get_computer_choice():
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    return computer_choice

def get_user_choice():
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    options = ['rock', 'paper', 'scissors']
    if user_choice in options:
        return user_choice
    else:
        print("Invalid choice, please enter rock, paper, or scissors")
        return get_user_choice()


def get_winner(computer_choice, user_choice):
    user_wins = 0
    computer_wins = 0
    while user_wins < 2 and computer_wins < 2:
        if computer_choice == user_choice:
            print("It's a tie!")
        elif computer_choice == 'rock' and user_choice == 'scissors':
            print("You lost!")
            computer_wins += 1
        elif computer_choice == 'paper' and user_choice == 'rock':
            print("You lost!")
            computer_wins += 1
        elif computer_choice == 'scissors' and user_choice == 'paper':
            print("You lost!")
            computer_wins += 1
        else:
            print("You won!")
            user_wins += 1
        print("Computer wins: {} User wins: {}".format(computer_wins,user_wins))
        computer_choice = get_computer_choice()
        user_choice = get_user_choice()
    if computer_wins == 3:
        print("Computer wins: 3")
        print("Computer wins the game!")
    else:
        print("User wins: 3")
        print("You win the game!")

def play():
    get_winner(get_user_choice(), get_computer_choice())

play()