"""
Author: [Natanya Anderson]
Assignment / Part: HW2 - Q2 (depending on the file name)
Date due: 2022-09-29, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

import math


frequency = float(input("Enter a value for the frequency, w: "))
duration = float(input("Enter a value for the duration of the sound wave, T: "))
equation = 2*math.sin(frequency*duration)/frequency
rounded = round(equation, 3)

answer = "The amplitude spectrum of this Fourier transform is: " + str(rounded)
print(answer)

