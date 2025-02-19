# Lesson 6 - Debugging

## Recap 1: Class Average Calculator

# You have been tasked to create a programme that calculates the
# average marks of a class.

# Your programme will have to ask the
# user for the total number of students, followed by the marks of
# each student one at a time.

# Use only variables, math operators that you have learnt, as# well as a 'for' loop
numStudents = int(input("how many students are there "))
sum = 0
for i in range(1,numStudents+1):
    sum=sum+int(input("what is student #" + "'s score"))
print("My sum is: " + str(sum)) 
print("my average is; " +str(sum/ numStudents))


# Tic-Tac-Toe Game (5x5)

# Function to display the board
def display_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * (len(board) * 4 - 1))
    print("\n")

# Function to check if a player has won
def check_winner(board, player):
    # Check rows, columns and diagonals
    for i in range(len(board)):
        if all([cell == player for cell in board[i]]):  # Check row
            return True
        if all([board[j][i] == player for j in range(len(board))]):  # Check column
            return True
    if all([board[i][i] == player for i in range(len(board))]):  # Check diagonal 1
        return True
    if all([board[i][len(board) - 1 - i] == player for i in range(len(board))]):  # Check diagonal 2
        return True
    return False

# Function to check if the board is full (a tie)
def board_full(board):
    return all([cell != " " for row in board for cell in row])

# Function for player's turn
def player_turn(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter a number (1-{len(board)*len(board)}): ")) - 1
            row, col = divmod(move, len(board))
            if board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("This spot is already taken, try again.")
        except (ValueError, IndexError):
            print(f"Invalid input! Please enter a number between 1 and {len(board)*len(board)}.")

# Main game loop
def play_game():
    size = 5  # Set board size (5x5)
    board = [[" " for _ in range(size)] for _ in range(size)]
    players = ["X", "O"]
    current_player = 0

    while True:
        display_board(board)
        player = players[current_player]
        player_turn(board, player)

        if check_winner(board, player):
            display_board(board)
            print(f"Player {player} wins!")
            break
        elif board_full(board):
            display_board(board)
            print("It's a tie!")
            break

        current_player = 1 - current_player  # Switch player

# Start the game
if __name__ == "__main__":
    play_game()
