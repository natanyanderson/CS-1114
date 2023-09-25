"""
Author: [Natanya Anderson]
Assignment / Part: HW3 - Q1 (depending on the file name)
Date due: 2022-10-06, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

current = float(input("Enter this user's current XP: "))
if current < 18.0:
    print("Level 1 Player (XP: " + str(current) + ")")
elif current >= 18.0 and current < 25:
    print("Level 2 Player (XP: " + str(current) + ")")
elif current >= 25.0 and current < 30:
    print("Level 3 Player (XP: " + str(current) + ")")
elif current >= 30.0 and current < 40:
    print("Level 4 Player (XP: " + str(current) + ")")
elif current >= 40.0 and current <= 50.0:
    print("Level 5 Player (XP: " + str(current) + ")")
else:
    print("ERROR: Please enter a valid XP value.")