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


        if not root in cords:
            cords[root] = {}

        note_list = list()
        for note in notes.split("-"):
            note_list.append(note)


        cords[root][cord_name] = note_list


        cord_line = file_handle_dictionary.readline()

    return cords

    file_handle_dictionary.close()


def get_possible_chords(note_list, dictionary):


    possible_cord_list = list()

    for root in dictionary:
        for cord_name in dictionary[root]:
            current_chord = dictionary[root][cord_name]
            if note_list[0] == current_chord[0]:

                check = all(item in current_chord for item in note_list)

                if check:

                    possible_cord_list.append(root + cord_name)

            possible_cord_list = tuple(possible_cord_list)

    return possible_cord_list


def get_chord_progression(chord_progression_file_name, chord_dictionary_file_name):

    chord_progression = list()
    try:
        file_handle_chord = open(chord_progression_file_name, "r")
    except FileNotFoundError:
        return chord_progression
    chord_dictionary = get_chord_dictionary(chord_dictionary_file_name)
    if len(chord_dictionary) == 0:
        return chord_progression

    cord_line = file_handle_chord.readline()
    while cord_line:
        notes_list = cord_line.strip().split(",")

        possible_chords = get_possible_chords(notes_list, chord_dictionary)

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
            if not output_string == "":
                output_string += "," + note
            else:
                output_string += note

        file_handle_output.write(output_string + "\n")

    progression = get_chord_progression("chord_progression.csv", "chords-normalised.csv")

    write_progression_file(progression, "my_file.csv")

