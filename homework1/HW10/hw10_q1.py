"""
Author: [Natanya Anderson]
Assignment / Part: HW10 - Q1
Date due: 2022-12-08, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

import random

class Instrument:
    def __init__(self, model, brand, strength):
        self.model = model
        self.brand = brand
        self.strength = strength

    def __repr__(self):
        return "{} {} ({} / 100 strength)".format(self.brand, self.model, self.strength*100)

    def does_break(self):
        rand_value = random.random()
        if rand_value < self.strength*0.5:
            return True
        else:
            return False
