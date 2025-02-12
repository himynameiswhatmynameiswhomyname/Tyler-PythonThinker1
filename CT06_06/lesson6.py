# Lesson 5 - Introduction to For Loop and range()

## Recap 1: Automated Birthday Invitation

# You run a small business that creates personalized digital
# birthday invitation cards. To automate the process, you decide
# to write a Python program. 

# This program should ask the user for:
# 1. birthday person's name
# 2. the age that they are turning that year
# 3. personal message from the sender

# Finally, the program prints out a personalized invitation
# message.

# ### Sample output:
# "Happy <Age>th birthday


## Task 1: Name Cheer

# Your school's Sports Day is coming up and you are coding a
# program to cheer your schoolmates up.

# Your program needs to:
# 1. Using input(), ask the user for their namee e.g. <Dave>
# 2. Print a cheer as shown below:
   
#     ### Example:
#     What is your name? [Input: "Dave"]
#     Give me a D!
#     Give me a a!
#     Give me a v!
#     Give me a e!
#     What do we have?
#     Dave is the best!

# Note:
#     Notice how "Give me a..." is repeated!
#     Which function should you be using\
# name = input("what is your name ")
# for x in name:
#    print("Give me a "+x +"!" )

# print("What do we have?")
# print(name +"is the best!")

       

## Task 2: Repeated Sentence Loop

# Print the sentence "I like chicken rice." 100 times using the
# 'for' loop

# for x in range(100):
#     print(x)

# **Task 6a**:
# Use a 'for' loop to print numbers from 2 to 24 in multiples of 2.
# for i in range(2,25,2):
#     print(i)
# **Task 6b**:
# Use a 'for' loop to print numbers from 8 to 96 in multiples of 8.
# for i in range(8,97,8):
#     print(i)
# **Task 6c**:
# Use a 'for' loop to print numbers from 5 to 1 in descending order.
# for i in range(5,0, -1):
#     print(i)

## Task 8: User-Defined Range Counter

# Using input(), ask the user for 2 numbers and store them in the
# variables:
# 1. start
# 2. stop

# Write a 'for' loop to count from **start** to **stop**
start=input("what number do you want to start?")
stop=input("what number do you want to stop")
for i in range(start),(stop):
    print(i)

# Note:
# What happens if the user inputs a higher start number than stop?
# Modify your code to be able to handle that scenario.