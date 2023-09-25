"""
Author: [Natanya Anderson]
Assignment / Part: HW9 - Q1
Date due: 2022-12-01, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

def get_chord_dictionary(chord_dictionary_file_name):
    cords = dict()

    try:
        file_handle_dictionary = open(chord_dictionary_file_name, "r")
    except FileNotFoundError:
        return cords

    header_line = file_handle_dictionary.readline()
    cord_line = file_handle_dictionary.readline()
    while cord_line:
        cord_splits = cord_line.split(",")
        root = cord_splits[0]
        cord_name = cord_splits[1]
        notes = cord_splits[2].strip()

        # IF root not in the cords output, make a new empty chords
        if not root in cords:
            cords[root] = {}

        note_list = list()
        for note in notes.split("-"):
            note_list.append(note)

            # Append the notes to the root+chord
        cords[root][cord_name] = note_list

        # Read the next line and go through loop again
        cord_line = file_handle_dictionary.readline()

    return cords

    file_handle_dictionary.close()


def get_possible_chords(note_list, dictionary):

    # Create an empty return list
    possible_cord_list = list()

   # if len(note_list) == 0:
     #   return possible_cord_list

    # Walk all music roots in dictionary
    for root in dictionary:
        # Loop through all chords in the root
        for cord_name in dictionary[root]:
            current_chord = dictionary[root][cord_name]

            # Check if the 1st note of the incoming note_list is also the 1st note in the current_chord
            if note_list[0] == current_chord[0]:
                # Check if all notes are in the current chord
                check = all(item in current_chord for item in note_list)

                if check:
                    # Yes all notes are in the current chord so add to the return list
                    possible_cord_list.append(root + cord_name)

            possible_cord_list = tuple(possible_cord_list)
    # Return the tuple
    return possible_cord_list


def get_chord_progression(chord_progression_file_name, chord_dictionary_file_name):
    # Create an empty return list
    chord_progression = list()
    try:
        # Check if the chord progression file exists
        file_handle_chord = open(chord_progression_file_name, "r")
    except FileNotFoundError:
        return chord_progression

     # chord_dictionary is the whole data structure in figure 4
    chord_dictionary = get_chord_dictionary(chord_dictionary_file_name)

    # Check if the chord dictionary has content
    if len(chord_dictionary) == 0:
        return chord_progression


     # Read and loop through each line of the chord progression file
    cord_line = file_handle_chord.readline()
    while cord_line:
        # strip the \n line returns and split the notes in this line of the file into a list
        notes_list = cord_line.strip().split(",")

        # get a list of the possible chords for this 1 line of the progression file
        possible_chords = get_possible_chords(notes_list, chord_dictionary)

        # Check if this line of the chord progression file had matches in the chord dictionary
        if len(possible_chords):
            chord_progression.append(possible_chords)

        cord_line = file_handle_chord.readline()

    return chord_progression

    file_handle_chord.close()


def write_progression_file(output_progression, output_filename):
    file_handle_output = open(output_filename, "w")

    for line in output_progression:
        output_string = ""
        for note in line:
            # If the line already has some output we need to prepend a comma
            if not output_string == "":
                output_string += "," + note
            else:
                output_string += note

        file_handle_output.write(output_string + "\n")

    progression = get_chord_progression("chord_progression.csv", "chords-normalised.csv")

    write_progression_file(progression, "my_file.csv")

