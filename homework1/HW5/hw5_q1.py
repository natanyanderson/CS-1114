"""
Author: [Natanya Anderson]
Assignment / Part: HW5 - Q1 (depending on the file name)
Date due: 2022-10-20, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

# Ask user for input
# Loop through string
# if alphabetical letter lowercase, incriment unchanged counter
# if alphabetical character uppercase, convert to lowercase and incriment change counter
# if non-alphabetical, incriment non-alphabetic counter
# Assume we can use chr and ord

statement_1 = input("Say something: ")
special_character_count = 0
change_character = 0
unchanged_character = 0
var = ord('A')
answer = ""
for i in statement_1:
    var = ord(i)
    if var >= 65 and var <= 91:
        var_2 = var + 32
        answer += chr(var_2)
        change_character += 1
    elif var >= 97 and var <= 122:
        answer += i
        unchanged_character += 1
    else:
        special_character_count += 1
        answer += i

print(answer)
print("Number of changed letters: " + str(change_character))
print("Number of unchanged letters: " + str(unchanged_character))
print("Number of non-alphabetic characters: " + str(special_character_count))