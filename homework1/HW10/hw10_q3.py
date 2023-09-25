"""
Author: [Natanya Anderson]
Assignment / Part: HW10 - Q3
Date due: 2022-12-08, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

import random

from hw10_q2 import Musician
from hw10_q1 import Instrument


def get_name_of_battle_winner(musician_one, musician_two):
    instrument_one = musician_one.pick_instrument()
    print(str(musician_one.stage_name) + " picked a " + str(instrument_one) + "!")
    instrument_two = musician_two.pick_instrument()
    print(str(musician_two.stage_name) + " picked a " + str(instrument_two) + "!")
    if instrument_one == None and instrument_two == None:
        return "NO CONTEST"
    strength_one = instrument_one.strength
    strength_two = instrument_two.strength
    if strength_one > strength_two:
        call_one = instrument_one.does_break()
        if call_one == True:
            print(musician_two.stage_name + "'s " + instrument_one.model + " broke!")
            return musician_one.stage_name
        else:
            return musician_two.stage_name
    elif strength_one < strength_two:
        call_two = instrument_two.does_break()
        if call_two == True:
            print(musician_one.stage_name + "'s " + instrument_two.model + " broke!")
            return musician_two.stage_name
        else:
            return musician_one.stage_name
    else:
        # 50/50 coin toss
        print("Both musician's instruments are the same strength. The winner will be decided by the whim of chance.")
        coin_toss = random.random()
        if coin_toss >= 0.0 and coin_toss < 0.6:
            return musician_one.stage_name
        else:
            return musician_two.stage_name

def main():
    danelectro = Instrument("Stock '59", "Danelectro", 0.25)
    fender_vi = Instrument("VI Bass", "Fender", 0.99)
    four_double_o_one = Instrument("4001C64 Bass", "Rickenbacker", 0.856)
    gear = [danelectro, fender_vi, four_double_o_one]
    # Let's say both musicians have access to the same gear
    sad_musician = Musician("Robert Smith", gear)
    less_sad_musician = Musician("Miki Berenyi", gear)
    # Testing the get_name_of_battle_winner method a few times
    number_of_duels = 10
    for duel_number in range(number_of_duels):
        winner_name = get_name_of_battle_winner(sad_musician, less_sad_musician)
        print(f"THE WINNER OF DUEL #{duel_number + 1} IS {winner_name}!",end="\n\n")
main()