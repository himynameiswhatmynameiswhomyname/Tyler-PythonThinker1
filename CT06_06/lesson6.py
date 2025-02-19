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


import random

def display_bridge(bridge, player_position):
    """Display the current state of the bridge with the player's position."""
    bridge_state = "".join(["[X]" if i == player_position else "[ ]" for i in range(len(bridge))])
    print("\n" + bridge_state + "\n")

def create_bridge(length):
    """Create a bridge with a given length, where half the tiles are safe (glass) and half are unsafe (broken)."""
    bridge = []
    for i in range(length):
        bridge.append(random.choice(['safe', 'broken']))
    return bridge

def play_game(bridge):
    """The player navigates through the bridge, selecting tiles to step on."""
    player_position = 0
    max_position = len(bridge) - 1

    while player_position < max_position:
        display_bridge(bridge, player_position)
        print(f"Step {player_position + 1} of {max_position + 1}: Choose the next tile to step on.")

        try:
            move = int(input(f"Choose tile {player_position + 2} (1 = safe, 2 = broken): "))
            if move == 1:  # Player chooses the "safe" option
                print("You chose the safe tile!")
                player_position += 1
                if bridge[player_position] == 'broken':
                    print("\nOops! You fell. The tile was broken. Game Over.")
                    break
            elif move == 2:  # Player chooses the "broken" option
                print("You chose the broken tile! Game Over.")
                break
            else:
                print("Invalid choice. Please enter 1 (safe) or 2 (broken).")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            
    if player_position == max_position:
        display_bridge(bridge, player_position)
        print("Congratulations! You completed the bridge successfully.")

def start_game():
    """Start the Glass Bridge game."""
    print("Welcome to the Glass Bridge Game from Squid Game!\n")
    bridge_length = 5  # You can change this for a longer bridge
    bridge = create_bridge(bridge_length)
    play_game(bridge)

# Start the game
if __name__ == "__main__":
    start_game()

