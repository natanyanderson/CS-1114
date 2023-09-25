"""
Author: [Natanya Anderson]
Assignment / Part: HW5 - Q2 (depending on the file name)
Date due: 2022-10-20, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

# Ask user for 2 inputs
# Fuse them together in alternating order
# Loop through each string. Loop range is maximum string length.
# If there is any letter that is not "A" "T" "C" "G", leave it out of sequence and have a counter for them
# Create a converted sequence with new sequence using DNA table
# Print out converted sequence and number of invalid letters

dna_1 = input("Enter a DNA sequence: ")
dna_2 = input("Enter a second DNA sequence: ")
invalid_character = 0
dna_converted = ""
length_one = len(dna_1)
length_two = len(dna_2)
max_length = max(length_one, length_two)
interleave_string = ""
for i in range(0, max_length):
    # is character index less than string one length
    if i < length_one:
        # index < length. add character to string
        interleave_string += dna_1[i]
    # is character index less than string two length
    if i < length_two:
         # index < length. add character to string
        interleave_string += dna_2[i]
#print(interleave_string)

for letter in interleave_string:
    if letter == "A":
        dna_converted += "T"
    elif letter == "C":
        dna_converted += "G"
    elif letter == "T":
        dna_converted += "A"
    elif letter == "G":
        dna_converted += "C"
    else:
        invalid_character += 1

print("Fused sequence:", dna_converted, "| Invalid characters:", invalid_character)
