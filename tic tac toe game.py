import random

# Function to print the current state of the board
def print_board(board):
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("\n")

# Function to check if a player has won
def check_win(board, player):
    # Check horizontal, vertical, and diagonal win conditions
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Function to check for a tie
def check_tie(board):
    return " " not in board

# Main game loop function
def play_game():
    print("Welcome to Tic-Tac-Toe!")

    board = [" "] * 9
    players = ["X", "O"]
    current_player = random.choice(players) # Randomly choose the first player
    print(f"Player {current_player} will go first.")

    while True:
        print_board(board)
        print(f"It's {current_player}'s turn.")

        try:
            move = int(input("Enter your move (1-9): ")) - 1 # Get player input (1-9 to match the board layout)

            if 0 <= move <= 8 and board[move] == " ":
                board[move] = current_player

                if check_win(board, current_player):
                    print_board(board)
                    print(f"*** Player {current_player} has won the game! ***")
                    break
                elif check_tie(board):
                    print_board(board)
                    print("*** It's a tie! ***")
                    break

                current_player = "O" if current_player == "X" else "X" # Switch player turns
            else:
                print("Invalid move. Try again.")

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    play_game()