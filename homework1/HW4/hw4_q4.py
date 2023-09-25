"""
Author: [Natanya Anderson]
Assignment / Part: HW4 - Q4 (depending on the file name)
Date due: 2022-10-06, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

# Ask user for positive integer
# With the input, print all numbers from 1 to input that have more even numbers than odd numbers.
# Example; 134 has 2 odd numbers (1,3) and 1 even number (4) so should not be printed.
# All numbers on one line seperated by spaces
# Must use %10 to get remainder and check remainder if negative or positive
# Must divide by 10 to get the next digit
num = int(input("Enter a positive integer: "))
i = 0
integer = 0
remainder = 0
even_count = 0
odd_count = 0
answer = ""
for i in range (1, num+1):
    var = i
    while var > 0:
        integer = var % 10
        if integer % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
     #   var = var//10
        var //=10
    if even_count > odd_count:
       # answer += str(i) + " "
      #  print(answer)
        print(i, end=" ")
    even_count = 0
    odd_count = 0




