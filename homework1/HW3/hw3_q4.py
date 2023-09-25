"""
Author: [Natanya Anderson]
Assignment / Part: HW3 - Q4 (depending on the file name)
Date due: 2022-10-06, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
import math


a = int(input("Please enter the value of a: "))
b = int(input("Please enter the value of b: "))
c = int(input("Please enter the value of c: "))
quadratic_equation_one = 0
quadratic_equation_two = 0
number_of_solutions = b ** 2 - 4 * a * c

# Check if divide by 0
if a == 0:
    if b == 0 and c == 0:
        print("Infinite number of solutions")
    else:
        print("No solution")
# Check if square root would be negative
elif number_of_solutions < 0:
    print("No real solutions")
else:
    quadratic_equation_one = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
    quadratic_equation_two = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
if quadratic_equation_one == quadratic_equation_two:
    print("This equation has 1 solution: x = " + str(quadratic_equation_one))
elif quadratic_equation_one != quadratic_equation_two:
    print("This equation has 2 solutions: x = " + str(quadratic_equation_one) + ", x = " + str(quadratic_equation_two))
