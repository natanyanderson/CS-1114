"""
Author: [Natanya Anderson]
Assignment / Part: HW8 - Q1 (depending on the file name)
Date due: 2022-11-17, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

from pprint import pprint

#function takes nucleotides string and return dictionary of frequency of letters
def get_nucleotide_frequencies(nucleotides):
    nucleotides_sequence = {"A": 0, "C": 0, "G": 0, "Junk": {}, "T": 0}
    counter_for_junk = 0
    for letter in nucleotides:
        letter = letter.upper()
        if letter == "A" or letter == "C" or letter == "G" or letter == "T":
            nucleotides_sequence[letter] = nucleotides_sequence[letter] + 1
        else:
            if letter not in nucleotides_sequence["Junk"]:
                nucleotides_sequence["Junk"][letter] = 1
                counter_for_junk += 1
            else:
                nucleotides_sequence["Junk"][letter] = nucleotides_sequence["Junk"][letter] + 1
                counter_for_junk += 1
    return nucleotides_sequence, counter_for_junk



def main():
    frequencies, junk_count = get_nucleotide_frequencies("ACTGTCaCGRFRTNfsHYCgggTCGACCSGTGTCACGT")
    pprint(frequencies)
    print(f"Number of junk nucleotides: {junk_count}.")

main()