"""
Author: [Natanya Anderson]
Assignment / Part: HW7 - Q4 (depending on the file name)
Date due: 2022-11-11, 12:00pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

from dance_dance_revolution import DanceDanceRevolution

GAME = DanceDanceRevolution()

def get_game_parameters():
    my_tuple = ()
    steps_memorized = int(input("How many steps would you like to memorize? (positive non-zero integers only) "))
    while steps_memorized <= 0:
        print("WARNING: Please enter a positive non-zero integer value.")
        steps_memorized = int(input("How many steps would you like to memorize? (positive non-zero integers only) "))

    speed_memorized = float(input("How fast would you like the game to run? (positive non-zero numerical values only) "))
    while speed_memorized <= 0:
        print("WARNING: Please enter a positive non-zero integer value.")
        speed_memorized = float(input("How fast would you like the game to run? (positive non-zero numerical values only) "))
    my_tuple = steps_memorized, speed_memorized
    return my_tuple




def get_user_answers():
    my_list = []
    direction = input("Enter a direction (U/D/L/R) or 'DONE' to finish: ")
    if direction == "DONE":
        print("Please enter at least one answer before selecting 'DONE'.")
        direction = input("Enter a direction (U/D/L/R) or 'DONE' to finish: ")
        my_list.append(direction)
    while direction != "DONE":
        my_list.append(direction)
        direction = input("Enter a direction (U/D/L/R) or 'DONE' to finish: ")
    return my_list


def run_game():
    # ask parameters
    parameters = get_game_parameters()
    steps = parameters[0]
    speed = parameters[1]
    # use parameters into GAME object
    GAME.set_amount(steps)
    GAME.set_speed(speed)
    # have GAME display the game
    GAME.play_sequence()
    # ask user input
    print("!")
    directions = get_user_answers()

    checking_answer = GAME.check_answers(directions)
    if checking_answer == True:
        print("Congratulations! You've guessed correctly!")
    else:
        print("Sorry, you lose.")

    # win / lose
run_game()