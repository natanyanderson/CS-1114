# Ask for pokemon level + speed. int values
# Determine if crtical hit by random num < threshold
# threshold = t = (Pokemon speed/2)
# if critical hit, do damage multiplier
# print damage multiplier
import random

level = int(input("What is this Pokémon's level? "))
speed = int(input("What is this Pokémon's speed? "))
random_num = random.randint(0, 255)
threshold_equation = speed/2
damage_multiplier = (2*level + 6) / (level + 6)

if threshold_equation < 0:
    threshold_equation == 0
elif threshold_equation > 255:
    threshold_equation == 255
    
if random_num < threshold_equation:
    print("The Pokémon's move will be " + str(round(damage_multiplier, 2)) + "x stronger!")
else:
    print("No critical hit")
