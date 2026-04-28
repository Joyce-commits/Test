# Rock Paper Scissor Game

import random
playing = True
choices = ['rock', 'paper', 'scissor']
print("Welcome to Rock Paper Scissor Game!")
while playing:
    user_choice = input("Enter your choice (rock, paper, scissor): ").lower()
    if user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissor.")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie! Try again.")
    elif (user_choice == 'rock' and computer_choice == 'scissor') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissor' and computer_choice == 'paper'):
        print("Congratulations! You win!")
        playing = False
        break
    else:
        print("You lose! Try again.")
    