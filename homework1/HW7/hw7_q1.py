"""
Author: [Natanya Anderson]
Assignment / Part: HW7 - Q1 (depending on the file name)
Date due: 2022-11-11, 12:00pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

def update_frequencies(old_frequencies, new_sequence):
    list = []
    count_a = new_sequence.count("A")
    count_c = new_sequence.count("C")
    count_g = new_sequence.count("G")
    count_t = new_sequence.count("T")
    print("Number of nucleotides added: A -> ",count_a, "| C -> ",count_c, "| T -> ",count_t, "| G -> ",count_g)
    find_num_one = old_frequencies[0][1]
    add_a = find_num_one + count_a
    list = [("A",add_a)]
    find_num_two = old_frequencies[1][1]
    add_c = find_num_two + count_c
    list += [("C",add_c)]
    find_num_three = old_frequencies[2][1]
    add_t = find_num_three + count_t
    list += [("T",add_t)]
    find_num_four = old_frequencies[3][1]
    add_g = find_num_four + count_g
    list += [("G",add_g)]
    return list


def main():
 old_frequencies = [("A", 20), ("C", 23), ("T", 125), ("G", 4)]
 new_sequence = "ACCCGTTA"
 new_frequencies = update_frequencies(old_frequencies, new_sequence)

 print(new_frequencies)

main()