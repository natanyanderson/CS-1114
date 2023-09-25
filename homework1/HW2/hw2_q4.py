"""
Author: [Natanya Anderson]
Assignment / Part: HW2 - Q4 (depending on the file name)
Date due: 2022-09-29, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

days_one = int(input("Please enter the number of days Semi has worked: "))
hours_one = int(input("Please enter the number of hours Semi has worked: "))
minutes_one = int(input("Please enter the number of minutes Semi has worked: "))
days_two = int(input("Please enter the number of days Daniel has worked: "))
hours_two = int(input("Please enter the number of hours Daniel has worked: "))
minutes_two = int(input("Please enter the number of minutes Semi has worked: "))

hours_in_day = 24
minutes_in_hour = 60
minutes_in_day = hours_in_day*minutes_in_hour

semi_total_minutes = (days_one*minutes_in_day) + (hours_one*minutes_in_hour) + (minutes_one)
daniel_total_minutes = (days_two*minutes_in_day) + (hours_two*minutes_in_hour) + (minutes_two)

total_minutes_both = semi_total_minutes+daniel_total_minutes
days = total_minutes_both//minutes_in_day
minutes_left = total_minutes_both%minutes_in_day
hours = minutes_left//minutes_in_hour
minutes = minutes_left%minutes_in_hour
answer = "The total time both of them worked together is: " + str(days) + " days, " + str(hours) + " hours and " + str(minutes) + " minutes."
print(answer)









