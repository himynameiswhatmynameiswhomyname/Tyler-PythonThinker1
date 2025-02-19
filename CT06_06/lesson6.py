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
def display_progress(stones_left, round_num, max_rounds):
    print(f"\nRound {round_num} of {max_rounds}:")
    print(f"You have {stones_left} stones left to play with.")
    print("Pick up the correct number of stones as instructed.")

# Function for Phase 1 (Basic Round)
def phase_1(stones_left):
    stones_to_pick = random.randint(1, stones_left)
    print(f"Pick up {stones_to_pick} stones!")
    return stones_to_pick

# Function for Phase 2 (Increasing Difficulty)
def phase_2(stones_left):
    stones_to_pick = random.randint(1, stones_left)
    print(f"Pick up {stones_to_pick} stones, but don't drop any!")
    time.sleep(1)
    return stones_to_pick

# Function for Phase 3 (Speed Round)
def phase_3(stones_left):
    stones_to_pick = random.randint(1, stones_left)
    print(f"Speed Round! Pick up {stones_to_pick} stones in 5 seconds!")
    time.sleep(1)
    start_time = time.time()
    while True:
        try:
            user_input = int(input("Pick up stones: "))
            if user_input == stones_to_pick:
                print(f"Correct! You picked up {stones_to_pick} stones.")
                break
            else:
                print("Incorrect! You lose 1 stone.")
                stones_left -= 1
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
        
    time_taken = time.time() - start_time
    if time_taken > 5:
        print(f"Too slow! You took {time_taken:.2f} seconds. You lose 1 stone.")
        stones_left -= 1
    return stones_left

# Function for Phase 4 (Multi-step Challenge)
def phase_4(stones_left):
    print("Multi-step Challenge!")
    steps = random.randint(2, 3)  # Random number of steps for multi-tasking
    total_stones_picked = 0
    for step in range(steps):
        print(f"\nStep {step + 1}:")
        stones_to_pick = random.randint(1, stones_left)
        print(f"Pick up {stones_to_pick} stones.")
        total_stones_picked += stones_to_pick
        if total_stones_picked > stones_left:
            print(f"Too many stones! You only have {stones_left} left.")
            stones_left = 0
            break
        stones_left -= stones_to_pick
    return stones_left

# Main game function to play all phases
def play_5_stones():
    total_stones = 5
    stones_left = total_stones
    round_num = 1
    max_rounds = 4

    print("Welcome to the Complicated 5 Stones Game from Squid Game!\n")
    time.sleep(1)
    print("You start with 5 stones.\n")
    time.sleep(1)
    
    while stones_left > 0 and round_num <= max_rounds:
        display_progress(stones_left, round_num, max_rounds)

        if round_num == 1:
            stones_to_pick = phase_1(stones_left)
        elif round_num == 2:
            stones_to_pick = phase_2(stones_left)
        elif round_num == 3:
            stones_left = phase_3(stones_left)
            if stones_left <= 0:
                break
            stones_to_pick = random.randint(1, stones_left)  # For simplicity, still random in phase 3
        elif round_num == 4:
            stones_left = phase_4(stones_left)
            if stones_left <= 0:
                break
            stones_to_pick = random.randint(1, stones_left)  # For simplicity, still random in phase 4

        try:
            user_guess = int(input(f"Pick up {stones_to_pick} stones: "))
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
        print("Congratulations! You have completed all rounds and picked up all the stones!")
    else:
        print("Game Over! You didn't complete the game successfully.")

# Start the game
if __name__ == "__main__":
    play_5_stones()



