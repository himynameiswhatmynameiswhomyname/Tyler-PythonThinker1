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
import time

# Function to display the game progress
def display_progress(stones_left, round_num):
    print(f"\nRound {round_num}:")
    print(f"You have {stones_left} stones left to play with.")
    print("Pick up the correct number of stones as instructed.")

# Function to simulate the 5 Stones Game
def play_5_stones():
    # Starting number of stones
    total_stones = 5
    stones_left = total_stones
    round_num = 1
    
    print("Welcome to the 5 Stones Game from Squid Game!\n")
    time.sleep(1)
    print("You start with 5 stones.\n")
    time.sleep(1)
    
    while stones_left > 0:
        display_progress(stones_left, round_num)
        
        # In each round, you need to pick up a random number of stones
        stones_to_pick = random.randint(1, stones_left)
        
        try:
            # Player guesses how many stones they should pick up
            user_guess = int(input(f"Pick up {stones_to_pick} stones: "))
            time.sleep(1)
            
            if user_guess == stones_to_pick:
                print(f"Correct! You picked up {stones_to_pick} stones.\n")
                stones_left -= stones_to_pick
                round_num += 1
            else:
                print(f"Wrong! You were supposed to pick up {stones_to_pick} stones. Game Over!")
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    if stones_left == 0:
        print("Congratulations! You have completed the 5 Stones Game!\n")
        print("You successfully picked up all the stones and completed all rounds.")

# Start the game
if __name__ == "__main__":
    play_5_stones()


