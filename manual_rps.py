import random

def get_computer_choice():

    choice_list = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choice_list)
    return computer_choice

def get_user_choice():
    user_choice = input("Please input 'rock', 'paper' or 'scissors': ")
    user_choice = user_choice.lower()
    if user_choice == "rock" or "paper" or "scissors":

        return user_choice

def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return print(f"Both players selected {user_choice}. It's a tie!")
        
    elif user_choice == "rock":
        if computer_choice == "scissors":
            return print("Rock smashes scissors! You win!")
        else:
            return print("Paper covers rock! You lose.")
    elif user_choice == "paper":
        if computer_choice == "rock":
            return print("Paper covers rock! You win!")
        else:
            return print("Scissors cuts paper! You lose.")
    elif user_choice == "scissors":
        if computer_choice == "paper":
            return print("Scissors cuts paper! You win!")
        else:
            return print("Rock smashes scissors! You lose.")

def play():
    get_winner(get_user_choice(), get_computer_choice())

play()