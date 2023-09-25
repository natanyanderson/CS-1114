"""
Author: [Natanya Anderson]
Assignment / Part: HW5 - Q3 (depending on the file name)
Date due: 2022-10-20, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

# Ask user for lower case letter sequence
# Determine if the input is decreasing or increasing in lexicographic order as you go through sequence
lower_case_letters = input("Please enter a string of lowercase letters: ")
not_decreasing = 0
save_num = ord("{")
counter = 0
var = ord('a')
var_2 = var + 25
var_3 = chr(var_2)
is_decreasing = True
not_decreasing = False
for i in lower_case_letters:
    var = ord(i)
    if var < save_num:
        counter += 1
        save_num = var
        is_decreasing = True
    else:
        is_decreasing = False
if is_decreasing == True:
    print(lower_case_letters + " is decreasing.")
if is_decreasing == False:
    print(lower_case_letters + " is not decreasing.")



#else:
    #print(lower_case_letters + " is not decreasing.")












