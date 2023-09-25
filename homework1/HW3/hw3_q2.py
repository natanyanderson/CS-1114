"""
Author: [Natanya Anderson]
Assignment / Part: HW3 - Q2 (depending on the file name)
Date due: 2022-10-06, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
import random

level = int(input("What is this Pokémon's level? "))
speed = int(input("What is this Pokémon's speed? "))
random_value = random.randint(0,255)
threshold_formula = speed/2
# Threshold formula is supposed to be between 0 and 255
if threshold_formula < 0:
    threshold_formula = 0
elif threshold_formula > 255:
    threshold_formula = 255
multiplier_formula = (2*level + 6) / (level + 6)

if random_value < threshold_formula:
    # I am rounding to two decimals because question wanted that
    print("The pokémon's move will be " + str(round(multiplier_formula, 2)) + "x stronger!")
else:
    print("No critical hit")

#elif random_value < threshold_value:
  # print("The pokémon's move will be" + str(multiplier_formula) + "x stronger!")



