import random

def get_user_choice():
    user_choice = input("Choose Rock, Paper, or Scissors: ").capitalize()
    while user_choice not in ['Rock', 'Paper', 'Scissors']:
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")
        print("===========================================")
        user_choice = input("Choose Rock, Paper, or Scissors: ").capitalize()
        print("===========================================")
    return user_choice

def get_computer_choice():
    return random.choice(['Rock', 'Paper', 'Scissors'])

def determine_winner(user_choice, computer_choice):
    print(f"You chose {user_choice}.")
    print("===========================================")
    print(f"The computer chose {computer_choice}.")
    print("===========================================")

    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == 'Rock' and computer_choice == 'Scissors') or
        (user_choice == 'Paper' and computer_choice == 'Rock') or
        (user_choice == 'Scissors' and computer_choice == 'Paper')
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    print("===========================================")

    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()
