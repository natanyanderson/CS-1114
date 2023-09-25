"""
Author: [Natanya Anderson]
Assignment / Part: HW4 - Q2 (depending on the file name)
Date due: 2022-10-06, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

# Ask user to input n
# Make a while loop that counts down from 2n-1
# Each printed string is 2n-1 long. This is a mix of stars and spaces. Use trick to repeat spaces and asterisks.
# Make a while loop that starts at 3 and counts up
# Each printed string is 2n-1 long.

num = int(input("Enter a positive integer: "))
i = 0
asterisks = "*"
white_space = " "
counter = 1
asterisks_count = (2 * num) - counter
while asterisks_count > 0:
   equation = (white_space * i) + (asterisks * asterisks_count) + (white_space * i)
   print(equation)
   i += 1
   counter -= -2
   asterisks_count = 2 * num - counter

# reset variables
i_two = 2
counter_two = 5
asterisks_count_two = (2 * num) - counter_two
while asterisks_count_two <= 2*num-1:
   equation_two = (white_space * i_two) + (asterisks * asterisks_count_two) + (white_space * i_two)
   print(equation_two)
   i_two -= 1
   counter_two += 2
   asterisks_count_two += 2
