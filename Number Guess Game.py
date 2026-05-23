import random

def start_game():
    # 1. Choose a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            # 2. Get user input and convert to integer
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            # 3. Check the guess against the secret number
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You found it in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter a whole number.")

if __name__ == "__main__":
    start_game()
