"""
Author: [Natanya Anderson]
Assignment / Part: HW2 - Q3 (depending on the file name)
Date due: 2022-09-29, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

import random
import math
max_hp = int(input("Enter a value for maximum amount of health point: "))
current_hp = random.randrange(1, max_hp)
Ball = random.randrange(0, 255)
equation_one = (max_hp*255*4)/(current_hp*Ball)
rounded_one = math.floor(equation_one)
generated = random.randrange(0, 255)
answer = rounded_one >= generated
print(answer)
