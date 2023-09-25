"""
Author: [Natanya Anderson]
Assignment / Part: HW4 - Q3 (depending on the file name)
Date due: 2022-10-06, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

# Ask user for positive integer
# Positive integer will represent how many rows of numbers are printed
# Positive integer will also represent last number printed in last row
# First line contains 1. Second line will contain 2,1. Third line is 3,2,1.
# If num is 5, 5,4,3,2,1 will be last numbers and last rows
# Assume input between one and nine. Check if num is 1-9.
# String length of each line is equal to num

num = int(input("Enter a positive integer (1-9): "))

i = 1
j = 1
n = 1
number_string = ""
white_space = ""
while i <= num:
    white_space_length = num - i
    while j <= white_space_length:
        white_space += " "
        j += 1
    while n <= i:
        number_string = str(n) + number_string
        n += 1
    equation = white_space + number_string
    print(equation)

    i += 1
    j = 1
    white_space = ""
    number_string = ""
    n = 1

