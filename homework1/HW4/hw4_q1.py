"""
Author: [Natanya Anderson]
Assignment / Part: HW4 - Q1 (depending on the file name)
Date due: 2022-10-06, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

# Print odd numbers for num amount of times. Starting from 1.
# Use a while loop and a for loop
num = int(input("Please enter a positive integer: "))
print("Executing while-loop...")
i = 0
counter = 1
while i < num:
    print(counter)
    i += 1
    counter += 2


print("Executing for-loop...")
counter = 1
for i in range(0, num):
    print(counter)
    counter += 2
