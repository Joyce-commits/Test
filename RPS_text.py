import random


def get_user_choice():
    choices = ["rock", "paper", "scissors"]
    while True:
        user_input = input("Choose Rock, Paper, or Scissors: ").strip().lower()
        if user_input in choices:
            return user_input
        else:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")


def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])


def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (
        (user == "rock" and computer == "scissors")
        or (user == "scissors" and computer == "paper")
        or (user == "paper" and computer == "rock")
    ):
        return "You win!"
    else:
        return "Computer wins!"


def play_game():
    print("=== Rock Paper Scissors ===")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(f"\nResult: {result}")


if __name__ == "__main__":
    while True:
        play_game()
        play_again = input("\nPlay again? (y/n): ").strip().lower()
        if play_again != "y":
            print("Thanks for playing!")
            break
