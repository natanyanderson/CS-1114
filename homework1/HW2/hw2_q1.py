"""
Author: [Natanya Anderson]
Assignment / Part: HW2 - Q1 (depending on the file name)
Date due: 2022-09-29, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

mass_first = int(input("Enter the mass of the first object: "))
radius_first = int(input("Enter the radius of the first object: "))
mass_second = int(input("Enter the mass of the second object: "))
radius_second = int(input("Enter the radius of the second object: "))
distance_of_objects = int(input("Enter the distance between the surfaces of both objects: "))
gravitational_constant = 6*10**-11
equation = ((mass_first*mass_second*gravitational_constant)/((radius_first+radius_second+distance_of_objects)**2))
answer = ("The force of gravitation between these two objects is " + str(equation) + " N.")
print(answer)


