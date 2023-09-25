"""
Author: [Natanya Anderson]
Assignment / Part: HW10 - Q2
Date due: 2022-12-08, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

from hw10_q1 import Instrument

import random

class Musician:
    def __init__(self, stage_name="", instruments=[]):
        self.stage_name = stage_name
        self.instruments = instruments
        self.number_of_instruments = len(instruments)

    def __str__(self):
        musician = "Musician object '{}', owning a ".format(self.stage_name)
        for index in range(self.number_of_instruments):
            if index == self.number_of_instruments - 1:
                musician += "and a " + str(self.instruments[index])
            else:
                musician += str(self.instruments[index]) + ", "
        return musician

    def pick_instrument(self, instrument_index=None):
        if self.number_of_instruments == 0:
            return None
        elif instrument_index == None:
            return random.choice(self.instruments)
        elif instrument_index >= self.number_of_instruments:
            return self.instruments[-1]
        else:
            return self.instruments[instrument_index]


