"""
Author: [Natanya Anderson]
Assignment / Part: HW7 - Q5 (depending on the file name)
Date due: 2022-11-11, 12:00pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

def get_matryoshka_list(original_list):
    new_list = []
    matryoshka_list = []
    for i in range(0, len(original_list)-1):
        if (original_list[i] < original_list[i + 1]):
            new_list.append(original_list[i])
            if (i == len(original_list) - 2):
                new_list.append(original_list[len(original_list) - 1])
                matryoshka_list.append(new_list)
        else:
            new_list.append(original_list[i])
            matryoshka_list.append(new_list)
            new_list = []
            if (i == len(original_list) - 2):
                new_list.append(original_list[len(original_list) - 1])
                matryoshka_list.append(new_list)

    return matryoshka_list


def main():
    original_list = [1, 2, 3, 5, 20, 19, 3, 4, 7, 45, 100, 1, 1, 3]
    matryoshka_list = get_matryoshka_list(original_list)

    print(matryoshka_list)

main()