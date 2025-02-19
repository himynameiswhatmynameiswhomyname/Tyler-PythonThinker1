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

def display_board(board):
    print("\n")
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("---------")
    print("\n")

# Function to check if a player has won
def check_winner(board, player):
    # Check rows, columns and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Check row
            return True
        if all([board[j][i] == player for j in range(3)]):  # Check column
            return True
    if all([board[i][i] == player for i in range(3)]):  # Check diagonal 1
        return True
    if all([board[i][2 - i] == player for i in range(3)]):  # Check diagonal 2
        return True
    return False

# Function to check if the board is full (a tie)
def board_full(board):
    return all([cell != " " for row in board for cell in row])

# Function for player's turn
def player_turn(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter a number (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("This spot is already taken, try again.")
        except (ValueError, IndexError):
            print("Invalid input! Please enter a number between 1 and 9.")

# Main game loop
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
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
