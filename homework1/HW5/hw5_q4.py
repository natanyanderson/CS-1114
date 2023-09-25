"""
Author: [Natanya Anderson]
Assignment / Part: HW5 - Q4 (depending on the file name)
Date due: 2022-10-20, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
# Ask user for notes. When user is done type "DONE"
# Ask user for direction. "U" is for UP and "D" is for down. if lowercase, it is invalid.
# Ask times user wants the arpeggiator to play. Must be a pos int.
# Output should be the times and direction user selected.

import arpeggiator

ARPEGGIATOR = arpeggiator.Arpeggiator()
UP = arpeggiator.Direction.UP
DOWN = arpeggiator.Direction.DOWN

note = input("Enter a musical note (i.e. A, Db, C#, etc.) or 'DONE' to end: ")
while note != "DONE":
    ARPEGGIATOR.add_note(note)
    note = input("Enter a musical note (i.e. A, Db, C#, etc.) or 'DONE' to end: ")
print()
print(ARPEGGIATOR)
print()

direction = input("Enter an arpeggiator direction [U/D] ")
while direction != "U" and direction != "D":
    direction = input("Enter an arpeggiator direction [U/D] ")
print()
times = int(input("How many times do you want your arpeggiator to play? "))
while times < 0:
    times = int(input("How many times do you want your arpeggiator to play? (Must be a positive amount) "))
print()

for i in range(times):
    if direction == "U":
        ARPEGGIATOR.play(UP)
    else:
        ARPEGGIATOR.play(DOWN)


