"""
Author: [Natanya Anderson]
Assignment / Part: HW2 - Q5 (depending on the file name)
Date due: 2022-09-29, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

permission_from_dean = input("Do you have permission from the dean? [y/n] ")
permission_from_advisor = input("Do you have permission from your advisor? [y/n] ")
senior_status = input("Do you hold senior status? [y/n] ")
credits = int(input("How many credits do you have? "))

circumstance_1 = (credits >= 64) and (senior_status == "y")
circumstance_2 = (credits >= 40) and (permission_from_advisor == "y")
circumstance_3 = permission_from_dean == "y"

answer = (circumstance_1 or circumstance_2 or circumstance_3)
print(answer)




