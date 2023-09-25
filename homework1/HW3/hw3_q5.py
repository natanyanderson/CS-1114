"""
Author: [Natanya Anderson]
Assignment / Part: HW3 - Q5 (depending on the file name)
Date due: 2022-10-06, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

# Get user inputs of 3 sides
# Find if all 3 sides are equal (Equilateral triangle)
# Check if two sides are equal and angle is 90 (Isoceles right triangle). x times sqrt2
# Check if two sides are equal and angle is not 90 (Isoceles not right triangle)
# Else: Scalene triangle
# Floating points can't be too far off (by not more than 0.00001)
import math

first_side = float(input("Length of first side: "))
second_side = float(input("Length of second side: "))
third_side = float(input("Length of third side: "))

if first_side == second_side and first_side == third_side:
    print(str(first_side) + ", " + str(second_side) + ", " + str(third_side) + " form an equilateral triangle")
elif first_side == second_side and first_side != third_side:
    my_calculation = first_side * math.sqrt(2)
    if abs(my_calculation - third_side) < 0.00001:
        print(str(first_side) + ", " + str(second_side) + ", " + str(third_side) + " form an isoceles right triangle")
    else:
        print(str(first_side) + ", " + str(second_side) + ", " + str(third_side) + " form an isoceles not right triangle")
elif first_side == third_side and first_side != second_side:
    my_calculation = first_side * math.sqrt(2)
    if abs(my_calculation - second_side) < 0.00001:
        print(str(first_side) + ", " + str(second_side) + ", " + str(third_side) + " form an isoceles right triangle")
    else:
        print(str(first_side) + ", " + str(second_side) + ", " + str(third_side) + " form an isoceles not right triangle")
elif third_side == second_side and first_side != third_side:
    my_calculation = third_side * math.sqrt(2)
    if abs(my_calculation - first_side) < 0.00001:
        print(str(first_side) + ", " + str(second_side) + ", " + str(third_side) + " form an isoceles right triangle")
    else:
        print(str(first_side) + ", " + str(second_side) + ", " + str(third_side) + " form an isoceles not right triangle")
else:
    print(str(first_side) + ", " + str(second_side) + ", " + str(third_side) + " form a scalene triangle")