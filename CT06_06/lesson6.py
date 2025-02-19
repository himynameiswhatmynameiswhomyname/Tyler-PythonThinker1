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
print("my average is; " +str(sum/ numofstudents))
